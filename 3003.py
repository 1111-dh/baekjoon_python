import sys
arr=list(map(int,sys.stdin.readline().split()))
chess=[1,1,2,2,2,8]
for i,j in zip(arr,chess):
    print(j-i,end=' ')