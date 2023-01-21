import sys
input=sys.stdin.readline
n=int(input())
dp = [i for i in range(n + 1)]
path= [i for i in range(n + 1)]
dp[1],path[1]=0,0
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    path[i] = i-1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        path[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        path[i] = i//2
print(dp[-1])
while n!=0:
    print(n,end=" ")
    n=path[n]

