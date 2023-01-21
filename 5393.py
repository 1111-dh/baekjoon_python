import sys
import math
input=sys.stdin.readline

# def templit(n,k):
#     if n==0 or n==1 or n==3:
#         return 2*k
#     else:
#         return 2*k+1
    
# t=int(input())
# for _ in range(t):
#     n=int(input())
#     tmp=0
#     if n==0:
#         print(0)
#     elif n==1 or n==2 or n==4:
#         print(1)
#     elif n==3:
#         print(2)
#     else:
#         print(math.ceil(n/2) + templit((n+1)%6,(n+1)//6))

import sys
input=sys.stdin.readline
  
t=int(input())
for _ in range(t):
    n=int(input())
    print((n+1)//2+(n+1)//2-((n-1)//3+1)//2)