import sys
from collections import deque
input=sys.stdin.readline

r,c,k=map(int,input().split())
mmap=[list(input().rstrip()) for _ in range(r)]
answer=0
dx=[0,1,0,-1]
dy=[1,0,-1,0]
visit=[[0]*c for _ in range(r)]

def dfs(x,y,dist):
    if x==c-1 and y==0:
        if dist==k:
            global answer
            answer+=1
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<c and 0<=ny<r and visit[ny][nx]==0:
            if mmap[ny][nx]=='.':
                visit[ny][nx]=1
                dfs(nx,ny,dist+1)
                visit[ny][nx]=0
visit[r-1][0]=1
dfs(0,r-1,1)
print(answer)
