import sys
input=sys.stdin.readline

L,C=map(int,input().split())
char=sorted(list(input().split()))

def back(idx,choose,cnt):
    if len(choose)==L:
        if cnt>=1 and L-cnt>=2:
            print(choose)
        return
    for i in range(idx,C):
        if char[i] in ['a','e','i','o','u']:
            back(i+1,choose+char[i],cnt+1)
        else:
            back(i+1,choose+char[i],cnt)

back(0,'',0)
#cnt==모음 수