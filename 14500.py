import sys
input=sys.stdin.readline
n,m=map(int,input().split())
lst=[list(map(int,input().split())) for _ in range(n)]
answer,MAX=0,max(map(max,lst))
visit=[[0]*m for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(x,y,L,res):
    global answer
    if answer>=res+MAX*(4-L):
        return
    if L==4:
        if answer<res:
            answer=res
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<m and 0<=ny<n and visit[ny][nx]==0:
            if L==2:
                visit[ny][nx]=1
                dfs(x,y,L+1,res+lst[ny][nx])
                visit[ny][nx]=0
            visit[ny][nx]=1
            dfs(nx,ny,L+1,res+lst[ny][nx])
            visit[ny][nx]=0
for i in range(n):
    for j in range(m):
        visit[i][j]=1
        dfs(j,i,1,lst[i][j])
        visit[i][j]=0
print(answer)
            
        
    
            
    
    
    