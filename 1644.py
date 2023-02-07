import sys
input=sys.stdin.readline

n=int(input())
prime=[0,0]+[1]*(n-1)
prime_list=[]
for i in range(2,n+1):
    if prime[i]:
        prime_list.append(i)
        for j in range(i*2,n+1,i):
            prime[j]=0
            
start,end,s,answer=0,0,0,0
long=len(prime_list)

while True:
    if s==n:
        answer+=1

    if s>n: 
        s-=prime_list[start]
        start+=1
    elif end==long:
        break
    else:
        s+=prime_list[end]
        end+=1

print(answer)