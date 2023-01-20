import sys
input=sys.stdin.readline
INF = 2147000000

n=int(input())
weight=[list(map(int,input().split())) for _ in range(n)]

ans=INF
for color in range(3):
  rgb=[[INF]*(n) for _ in range(3)]
  rgb[color][0] = weight[0][color]
  for i in range(1,n):
    rgb[0][i]=min(rgb[1][i-1],rgb[2][i-1])+weight[i][0]
    rgb[1][i]=min(rgb[0][i-1],rgb[2][i-1])+weight[i][1]
    rgb[2][i]=min(rgb[0][i-1],rgb[1][i-1])+weight[i][2]

  for j in range(3):
    if color != j:
      ans = min(ans, rgb[j][-1])
print(ans)