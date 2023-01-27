import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

m,n=map(int,input().split())
Map=[list(map(int,input().split())) for _ in range(m)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
dp=[[-1]*n for _ in range(m)]

def dfs(x,y):
    global visit
    if x==n-1 and y==m-1:
        return 1
    if dp[y][x]!=-1:
        return dp[y][x]
    route=0
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<n and 0<=ny<m and Map[y][x]>Map[ny][nx]:
            route+=dfs(nx,ny)
    dp[y][x]=route
    return route

print(dfs(0,0))

