import sys
input=sys.stdin.readline

n=int(input())
print(" "*(n-1)+"*")
for i in range(2,n+1):
    print(" "*(n-i) + "*" + " "*(i*2-3) + "*")