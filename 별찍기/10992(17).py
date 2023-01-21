import sys
input=sys.stdin.readline

n=int(input())
print(" "*(n-1)+"*")
if n!=1:
    for i in range(2,n):
        print(" "*(n-i) + "*" + " "*(i*2-3) + "*")
    print("*"*(n*2-1))