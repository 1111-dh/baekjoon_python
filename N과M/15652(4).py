from itertools import combinations_with_replacement
import sys
n,m=map(int,sys.stdin.readline().split())
lst=[i for i in range(1,n+1)]
for i in list(map(list,combinations_with_replacement(lst,m))):
    for j in i:
        print(j,end=" ")
    print()