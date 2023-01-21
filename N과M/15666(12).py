import sys
input=sys.stdin.readline

def perm(i,n,m,s,tmp):
    if i==m:
        print(*tmp)
        return
    prev=0
    for j in range(n):
        if (i==0 or tmp[i-1]<=s[j]) and prev!=s[j]:
            tmp.append(s[j])
            prev=s[j]
            perm(i+1,n,m,s,tmp)
            tmp.pop()
            
n,m=map(int,input().split())
s=sorted(list(map(int,input().split())))

perm(0,n,m,s,[])