import sys
input=sys.stdin.readline

def star(n):
    if n==1:
        return ["*"]
    S=star(n-1)
    L=[]
    tmp=len(S[0])
    L.append("*"*(tmp+4))
    L.append("*"+ " "*(tmp+2) +"*")
    for i in S:
        L.append("* " + i + " *")
    L.append("*"+ " "*(tmp+2) +"*")
    L.append("*"*(tmp+4))
    return L
      
n=int(input())
print("\n".join(star(n)))