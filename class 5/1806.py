import sys
input=sys.stdin.readline

n,s=map(int,input().split())
arr=list(map(int,input().split()))
m,start,end,sigma=9999999999,0,0,0

while True:
    if sigma<s:
        if end==n:
            break
        sigma+=arr[end]
        end+=1
    else:
        m=min(end-start,m)
        sigma-=arr[start]
        start+=1

print(0 if m==9999999999 else m)