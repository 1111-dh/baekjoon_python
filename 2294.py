import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
DP=[999999]*(k+1)
for i in coin:
    if i<=k:
        DP[i]=1

for i in coin:
    for j in range(1,k+1):
        if j-i>0:
            DP[j]=min(DP[j-i]+1, DP[j])
            
print(DP[-1] if DP[-1]!=999999 else -1)