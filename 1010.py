import sys
input=sys.stdin.readline
def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    print(fact(m)//(fact(n)*fact(m-n)))
    