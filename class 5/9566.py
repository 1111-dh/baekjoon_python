import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

t=int(input())

def dfs(idx):
    global result
    visit[idx]=1
    cycle.append(idx)
    i=arr[idx]
    
    if visit[i]:
        if i in cycle:
            result+=cycle[cycle.index(i):]
    else:
        dfs(i)
            
for _ in range(t):
    n=int(input())
    arr=[0]+list(map(int,input().split()))
    visit=[0]*(n+1)
    result=[]
    for i in range(1,n+1):
        if not visit[i]:
            cycle=[]
            dfs(i)
    print(n-len(result))
    