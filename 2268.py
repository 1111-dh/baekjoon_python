import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[0]*n
tree=[0]*4*n

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

for _ in range(m):
    a,b,c=map(int,input().split())
    if a==1:
        update(0,n-1,1,b-1,c)
        arr[b-1]=c
    else:
        if b>c: b,c=c,b
        print(interval_sum(0,n-1,1,b-1,c-1))
            