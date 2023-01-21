from itertools import product
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
lst=list(map(int,input().split()))
for i in sorted(list(product(lst,repeat=m))):
    if i==tuple(sorted(i)):
        for j in i:
            print(j,end=" ")
        print()