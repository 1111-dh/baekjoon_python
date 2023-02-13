import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=[int(input()) for _ in range(n)]
tree=[0]*4*n


def set_tree(start,end,idx):
    if start==end:
        tree[idx]=(arr[start],arr[start])
        return (arr[start],arr[start])
    mid=(start+end)//2
    tmp1=set_tree(start,mid,idx*2)
    tmp2=set_tree(mid+1,end,idx*2+1)
    tree[idx]=(min(tmp1[0],tmp2[0]),max(tmp1[1],tmp2[1]))
    return tree[idx]

def interval(start,end,idx,left,right):
    if start>right or end<left:
        return (1000000000,0)
    if start>=left and end<=right:
        return tree[idx]
    mid=(start+end)//2
    tmp1=interval(start,mid,idx*2,left,right)
    tmp2=interval(mid+1,end,idx*2+1,left,right)
    return (min(tmp1[0],tmp2[0]),max(tmp1[1],tmp2[1]))
    
set_tree(0,n-1,1)

for _ in range(m):
    a,b=map(int,input().split())
    print(*interval(0,n-1,1,a-1,b-1))

            