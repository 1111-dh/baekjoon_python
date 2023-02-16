import sys
from collections import deque
input=sys.stdin.readline

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs(x,y,key):
    answer=0
    if building[y][x]=="$":
        answer+=1
    elif ord('a')<=ord(building[y][x])<=ord('z'):
        key.append(building[y][x])
    else:
        if chr(ord(building[y][x])+32) not in key:
            return answer
    q=deque([x,y])
    while q:
        a,b=q.pop()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<=w+2 and 0<=ny<=h+2 and building[ny][nx]!='*':
                if building[ny][nx]=='$':
                    answer+=1
                    q.append([ny,nx])
                elif building[ny][nx]=='.':
                    q.append([ny,nx])
                elif ord('a')<=ord(building[ny][nx])<=ord('z'):
                    key.append(building[ny][nx])
                    building[ny][nx]='.'
                    q.append([ny,nx])
                else:
                    if chr(ord(building[ny][nx])+32) in key:
                        q.append([ny,nx])
                        building[ny][nx]='.'
    return answer
                
t=int(input())
for _ in range(t):
    h,w=map(int,input().split())
    building=['.']*(w+2)+[['.']+list(input().rstrip())+['.'] for _ in range(h)]+['.']*(w+2)
    key=list(input().rstrip())
    print(bfs(0,0,key))
    
    
    