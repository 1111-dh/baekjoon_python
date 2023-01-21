import sys
from collections import deque
def bfs(n,end):
    q=deque()
    visit=[0]*10000
    q.append((n,''))
    while q:
        n,com=q.popleft()
        if n==end:
            print(com)
            break
        dd=2*n if 2*n<9999 else 2*n%10000
        ss=n-1 if n else 9999
        ll=10*(n%1000) + n//1000
        rr=(n%10)*1000 + n//10
        if not visit[dd]:
            visit[dd]=1
            q.append((dd,com+'D'))
        if not visit[ss]:
            visit[ss]=1
            q.append((ss,com+'S'))
        if not visit[ll]:
            visit[ll]=1
            q.append((ll,com+'L'))
        if not visit[rr]:
            visit[rr]=1
            q.append((rr,com+'R'))   
            
t=int(sys.stdin.readline())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    bfs(a,b)
    