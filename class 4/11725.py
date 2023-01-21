import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(G,n,visit):
    for i in G[n]:
        if not visit[i]:
            visit[i]=n
            dfs(G,i,visit)

n=int(input())
G={i:[] for i in range(1,n+1)}
for _ in range(n-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
visit=[1,1]+[0]*(n-1)
dfs(G,1,visit)

for i in range(2,n+1):
    print(visit[i])


    