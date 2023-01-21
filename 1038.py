import sys
input=sys.stdin.readline

n=int(input())
if n>1023:
    print(-1)
    exit(1)
lst=[0]*1024
cnt,i=0,0
while cnt<n:
    tmp=str(i)
    l=len(tmp)
    for j in range(l-1):
        if tmp[j]<=tmp[j+1]:
            break 
    else:
        lst[cnt]=i
        print(cnt)
        cnt+=1
    i+=1
print(lst)