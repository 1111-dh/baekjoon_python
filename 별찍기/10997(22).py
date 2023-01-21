import sys
input=sys.stdin.readline

def star(n):
    if n==1:
        return ["*"]
    if n==2:
        return ["*****","*    ","* ***","* * *","* * *","*   *","*****"]
    S=star(n-1)
    L=[]
    tmp=len(S[0])
    L.append("*"*(tmp+4))
    L.append("*"+ " "*(tmp+3))
    L.append("* " + S[0] + "**")
    for i in range(1,len(S)):
        L.append("* " + S[i] + " *")
    L.append("*"+ " "*(tmp+2) +"*")
    L.append("*"*(tmp+4))
    return L
      
n=int(input())
a=star(n)
for i in range(len(a)):
    print(a[i] if i!=1 else "*")