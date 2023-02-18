import sys
input=sys.stdin.readline

n,m,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]
tree=[0]*4*n

def set_tree(start,end,idx):
    if start==end:
        tree[idx]=arr[start]
        return arr[start]
    mid=(start+end)//2
    tree[idx]=set_tree(start,mid,idx*2)+set_tree(mid+1,end,idx*2+1)
    return tree[idx]

def interval_sum(start,end,idx,left,right):
    if start>right or end<left:
        return 0
    if start>=left and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return interval_sum(start,mid,idx*2,left,right)+interval_sum(mid+1,end,idx*2+1,left,right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    tree[index] += value
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    
set_tree(0,n-1,1)

for _ in range(m+k):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,n-1,1,b-1,c-arr[b-1])
        arr[b-1]=c
    else:
        print(interval_sum(0,n-1,1,b-1,c-1))
        
            