from collections import deque
import sys
input=sys.stdin.readline

def bfs(lst,visit,x,y,n,m):
    cnt=0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    que=deque()
    que.append((x,y))
    bw=lst[y][x]
    while que:
        node=que.popleft()
        cnt+=1
        for i in range(4):
            nx=node[0]+dx[i]
            ny=node[1]+dy[i]
            if 0<=nx<n and 0<=ny<m and ((nx,ny) not in visit) and bw==lst[ny][nx]:
                visit.append((nx,ny))
                que.append((nx,ny))
    return bw,cnt
                          
n,m=map(int,input().split())
arr=[list(input().rstrip()) for _ in range(m)]
visit=[]
B,W=0,0
for i in range(m):
    for j in range(n):
        if (j,i) not in visit:
            visit.append((j,i))
            a,b=bfs(arr,visit,j,i,n,m)
            if a=='B':
                B+=b**2
            else:
                W+=b**2
print(W,B)
            

