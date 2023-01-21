import sys
from collections import deque
input=sys.stdin.readline

dx=[0,-1,0,1]
dy=[1,0,-1,0]

def bfs(xx,yy,size,lst,n):
    dist=[[0]*n for _ in range(n)]
    visit=[[0]*n for _ in range(n)]
    que=deque()
    que.append((xx,yy))
    re=[]
    while (que):
        x,y=que.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and visit[ny][nx]==0:
                if lst[ny][nx]<=size:
                    visit[ny][nx]=1
                    que.append((nx,ny))
                    dist[ny][nx]=dist[y][x]+1
                    if 0<lst[ny][nx]<size:
                        re.append((nx,ny,dist[ny][nx]))
    return sorted(re,key=lambda x:(-x[2],-x[1],-x[0]))


n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
size,cnt,answer=2,0,0

for i in range(n):
    for j in range(n):
        if lst[i][j]==9:
            lst[i][j]=0
            x,y=j,i
           
while True:
    tmp=bfs(x,y,size,lst,n)
    if len(tmp)==0:
        break
    nx,ny,distance=tmp.pop()
    
    answer+=distance
    lst[y][x],lst[ny][nx]=0,0
    x,y=nx,ny

    cnt+=1
    if cnt==size:
        cnt=0
        size+=1
    
print(answer)

