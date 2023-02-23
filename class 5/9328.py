import sys
from collections import deque
input=sys.stdin.readline

dx=[0,1,0,-1]
dy=[1,0,-1,0]
def bfs():
    visit=[[0]*(w+2) for _ in range(h+2)]
    answer=0
    q=deque()
    q.append((0,0))
    visit[0][0]=1
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<w+2 and 0<=ny<h+2 and building[ny][nx]!='*' and visit[ny][nx]==0:
                if building[ny][nx]=='$':
                    answer+=1
                    building[ny][nx]='.'
                elif ord('a')<=ord(building[ny][nx])<=ord('z'): #열쇠
                    key[ord(building[ny][nx])-ord('a')]=1
                    q = deque()
                    visit=[[0]*(w+2) for _ in range(h+2)]
                    building[ny][nx]='.'
                elif ord('A')<=ord(building[ny][nx])<=ord('Z'): #문
                    if key[ord(building[ny][nx])-65]==1: 
                        building[ny][nx]='.'
                    else: continue
                q.append((nx,ny))
                visit[ny][nx]=1
    return answer
            
                
t=int(input())
for _ in range(t):
    h,w=map(int,input().split())
    building = [list('.' + input().rstrip() + '.') for _ in range(h)]
    building = [['.'] * (w + 2)] + building + [['.'] * (w + 2)]
    key=[0]*26
    tmp=input().rstrip()
    if tmp!='0':
        for i in tmp:
            key[ord(i)-ord('a')]=1
            
    print(bfs())
    
    
    