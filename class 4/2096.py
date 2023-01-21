import sys
input=sys.stdin.readline

n=int(input())
weight=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(n) for _ in range(3)]
dp[0][0]=weight[0][0]
dp[1][0]=weight[0][1]
dp[2][0]=weight[0][2]
for i in range(1,n):
    dp[0][i]=max(dp[1][i-1],dp[0][i-1])+weight[i][0]
    dp[1][i]=max(dp[0][i-1],dp[2][i-1],dp[1][i-1])+weight[i][1]
    dp[2][i]=max(dp[2][i-1],dp[1][i-1])+weight[i][2]  
print(max(dp[0][-1],dp[1][-1],dp[2][-1]),end=" ")

for i in range(1,n):
    dp[0][i]=min(dp[1][i-1],dp[0][i-1])+weight[i][0]
    dp[1][i]=min(dp[0][i-1],dp[2][i-1],dp[1][i-1])+weight[i][1]
    dp[2][i]=min(dp[2][i-1],dp[1][i-1])+weight[i][2]  

print(min(dp[0][-1],dp[1][-1],dp[2][-1]))