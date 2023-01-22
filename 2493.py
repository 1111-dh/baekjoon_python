import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
stack=[]
for i in range(n):
    for j in range(i-1,-1,-1):
        if arr[j]>arr[i]:
            stack.append(j+1)
            break
    else:
        stack.append(0)

print(*stack)