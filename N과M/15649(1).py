import sys
input=sys.stdin.readline

n,m=map(int,input().split())
arr=list(range(1,n+1))
def back(depth,tmp,visit):
    if depth==m:
        print(*tmp)
        return
    prev=0
    for i in range(n):
        if visit[i]==0 and arr[i]!=prev:
            prev=arr[i]
            tmp.append(arr[i])
            visit[i]=1
            back(depth+1,tmp,visit)
            visit[i]=0
            tmp.pop()
back(0,[],[0]*n)