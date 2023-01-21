import sys
input=sys.stdin.readline

def perm(i,n,m,s,tmp):
    if i==m:
        print(" ".join(list(map(str,tmp))))
    else:
        for j in range(n):
            tmp.append(s[j])
            perm(i+1,n,m,s,tmp)
            tmp.pop()
            
n,m=map(int,input().split())
s=list(range(1,n+1))
perm(0,n,m,s,[])