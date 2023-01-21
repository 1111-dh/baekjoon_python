import sys
input=sys.stdin.readline

n=int(input())
G=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,input().split())
    G[a].append(b)
    G[b].append(a)