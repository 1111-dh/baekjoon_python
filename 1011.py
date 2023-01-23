import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    n=0
    while b-a > n*(n+1):
        n+=1
    print(n*2-1 if b-a <= n**2 else n*2)