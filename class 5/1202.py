import sys
import heapq
input=sys.stdin.readline

n,k=map(int,input().split())
gem=[list(map(int,input().split())) for _ in range(n)]
bag=[int(input()) for _ in range(k)]
gem.sort()
bag.sort()

heap=[]
answer=0
for i in bag:
    while gem and i>=gem[0][0]:
        heapq.heappush(heap,-heapq.heappop(gem)[1])
    if heap: answer-=heapq.heappop(heap)
print(answer)