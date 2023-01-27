import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m,k=map(int,input().split())
dx=[0,1,0,-1]
dy=[1,0,-1,0]

trash=[[0]*m for _ in range(n)]
visit=[[1]*m for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    trash[a-1][b-1]=1

cnt=0
def dfs(x,y):
    global cnt
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<m and 0<=ny<n and trash[ny][nx] and visit[ny][nx]:
            visit[ny][nx]=0
            cnt+=1
            dfs(nx,ny)

answer=0
for i in range(n):
    for j in range(m):
        if visit[i][j] and trash[i][j]:
            cnt=0
            dfs(j,i)
            if cnt>answer:
                answer=cnt
print(answer)
