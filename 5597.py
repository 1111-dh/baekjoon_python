import sys
input = sys.stdin.readline

dp=[0]*31
for _ in range(28):
    dp[int(input())]=1
for i in range(1,31):
    if dp[i]==0:
        print(i)