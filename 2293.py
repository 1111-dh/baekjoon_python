import sys
input=sys.stdin.readline

n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
DP=[0]*(k+1)
for i in range(1,k+1):
    for j in coin:
        if i-j>=0:
            DP[i]+=DP[i-j]+1
print(DP)