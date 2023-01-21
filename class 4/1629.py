import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())

def multiple(n):
    if n==1:
        return a%c
    tmp=multiple(n//2)
    if n%2:
        return tmp*tmp*a%c
    else:
        return tmp*tmp%c
print(multiple(b))