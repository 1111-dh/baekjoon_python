import sys
input=sys.stdin.readline

arr=list(input().rstrip())
stack=[]
cnt=0

for i in arr:
    if i.isdigit():
        cnt+=1
        tmp=int(i)
    elif i=="(":
        stack.append((tmp,cnt-1))
        cnt=0
    else:
        a,b=stack.pop()
        cnt=cnt*a+b

print(cnt)
        


    