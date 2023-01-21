import sys
n=int(sys.stdin.readline())
street=sys.stdin.readline().rstrip()
flag={'B':'J','O':'B','J':'O'}
dp=[999999999]*n
dp[0]=0
for i in range(1, n):
    for j in range(i):
        if street[j] == flag[street[i]]:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)
print(dp[n - 1] if dp[n - 1] != 999999999 else -1)