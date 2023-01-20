import sys
input=sys.stdin.readline

r,c=map(int,input().split())
alpha=[input().rstrip() for _ in range(r)]
visit=[[0]*c for _ in range(r)]
visit[0][0]=1
dx=[0,1,0,-1]
dy=[1,0,-1,0]
answer=0

def back(depth,x,y,visit,tmp):
  global answer
  if depth>answer:
    answer=depth

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<c and 0<=ny<r:
      if tmp[ord(alpha[ny][nx])-65]==0:
        if visit[ny][nx]==0:
          tmp[ord(alpha[ny][nx])-65]=1
          visit[ny][nx]=1
          back(depth+1,nx,ny,visit,tmp)
          visit[ny][nx]=0
          tmp[ord(alpha[ny][nx])-65]=0
tmp=[0]*26
tmp[ord(alpha[0][0])-65]=1
back(0,0,0,visit,tmp)       
print(answer+1)