import sys
input=sys.stdin.readline

n=int(input())
arr=sorted(list(map(int,input().split())))
m=9999999999

left,right=0,n-1
while left<right:
    tmp=arr[left]+arr[right]
    if abs(tmp)<m:
        m=abs(tmp)
        answer=[arr[left],arr[right]]
    
    if tmp<0:
        left+=1
    elif tmp>0:
        right-=1
    else:
        break
print(*answer)

