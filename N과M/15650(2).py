from itertools import combinations
import sys
n,m=map(int,sys.stdin.readline().split())
lst=[i for i in range(1,n+1)]
for i in list(map(list,combinations(lst,m))):
    for j in i:
        print(j,end=" ")
    print()