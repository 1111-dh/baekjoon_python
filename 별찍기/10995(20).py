import sys
input=sys.stdin.readline
      
n=int(input())
for i in range(1,n+1):
    print("* "*n if i%2 else " *"*n)