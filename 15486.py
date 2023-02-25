import sys
input = sys.stdin.readline

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dp=[0]*(n+2)

for i in range(1,n+1):
    if dp[i] < dp[i-1]:
        dp[i] = dp[i-1]
    if i+arr[i-1][0]<=n+1:
        if dp[i+arr[i-1][0]] < dp[i]+arr[i-1][1]:
            dp[i+arr[i-1][0]] = dp[i]+arr[i-1][1]
print(max(dp))