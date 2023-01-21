import sys
from collections import deque
def bfs(visit,q):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt=0
    while q:
        cnt+=1
        for _ in range(len(q)):
            a,b,c=q.popleft()
            for i in range(4):
                nx = b + dx[i]
                ny = a + dy[i]
                nh = c
                if 0 <= nx < m and 0 <= ny < n and 0 <= nh < h and visit[nh][ny][nx] == 0:
                    visit[nh][ny][nx] = 1
                    q.append([ny,nx,nh])
            if 0 <= c-1 < h and visit[c-1][a][b] == 0:
                visit[c-1][a][b] = 1
                q.append([a,b,c-1])
            if 0 <= c+1 < h and visit[c+1][a][b] == 0:
                visit[c+1][a][b] = 1
                q.append([a,b,c+1])
    return cnt
m, n ,h= map(int, sys.stdin.readline().split())
lst = [[[0]*m for row in range(n)] for depth in range(h)]
que=deque([])
for i in range(h):
    for j in range(n):
        lst[i][j]=list(map(int, sys.stdin.readline().split()))
for k in range(h):
    for i in range(n):
        for j in range(m):
            if lst[k][i][j] == 1:
                que.append([i,j,k])
count=bfs(lst,que)-1
for z in range(h):
    for y in range(n):
        for x in range(m):
            if lst[z][y][x] == 0:
                print(-1)
                exit()
print(count)