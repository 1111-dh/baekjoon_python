import sys
input=sys.stdin.readline

n=int(input())
tmp=2*n-3
print("*"*n + " "*(tmp) + "*"*n)
for i in range(1,n-1):
    print(" "*i + "*" + " "*(n-2) + "*" + " "*(tmp-i*2) + "*" + " "*(n-2) + "*")
print(" "*(n-1) + "*" + " "*(n-2) + "*" + " "*(n-2) + "*") 
for i in range(n-2,0,-1):
    print(" "*i + "*" + " "*(n-2) + "*" + " "*(tmp-i*2) + "*" + " "*(n-2) + "*")
print("*"*n + " "*(tmp) + "*"*n)