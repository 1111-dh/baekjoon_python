import sys
input=sys.stdin.readline
answer=9999999
def ab(a,b,cnt):
    if a==b:
        global answer
        if answer>cnt:
            answer=cnt
        return
    elif a>b:
        return
    ab(a*2,b,cnt+1)
    ab(a*10+1,b,cnt+1)
a,b=map(int,input().split())
ab(a,b,0)
print(-1 if answer==9999999 else answer+1)