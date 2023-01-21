import sys
input=sys.stdin.readline

n=int(input())
weight=[list(map(int,input().split())) for _ in range(n)]
rgb=[[0]*(n) for _ in range(3)]
rgb[0][0]=weight[0][0]
rgb[1][0]=weight[0][1]
rgb[2][0]=weight[0][2]
for i in range(1,n):
    rgb[0][i]=min(rgb[1][i-1],rgb[2][i-1])+weight[i][0]
    rgb[1][i]=min(rgb[0][i-1],rgb[2][i-1])+weight[i][1]
    rgb[2][i]=min(rgb[0][i-1],rgb[1][i-1])+weight[i][2]

print(min(rgb[0][-1],rgb[1][-1],rgb[2][-1]))