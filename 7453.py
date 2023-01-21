import sys
input=sys.stdin.readline

n=int(input())
a,b,c,d=[0]*n,[0]*n,[0]*n,[0]*n
x={}
for i in range(n):
    a[i],b[i],c[i],d[i]=map(int,input().split()) 
for i in a:
    for j in b:
        if x.get(i+j):
            x[i+j]+=1
        else:
            x[i+j]=1 
cnt=0
for i in c:
    for j in d:
        key=i+j
        if x.get(-key):
            cnt += x[-key]
print(cnt)