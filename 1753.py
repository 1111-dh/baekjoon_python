import sys
import heapq
input=sys.stdin.readline

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[int(1e9)]*(n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def dijkstra(x):
  distance[x]=0
  q = [(0, x)]

  while q:
      w, cur = heapq.heappop(q)
      if distance[cur] < w: 
          continue
      for dest, wei in graph[cur]:
          cost = distance[cur] + wei
          if distance[dest] > cost:
              distance[dest] = cost
              heapq.heappush(q, (cost, dest))
dijkstra(start)
for i in range(1,n+1):
    if distance[i]==int(1e9): print("INF")
    else: print(distance[i])