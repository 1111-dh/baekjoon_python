import sys
input=sys.stdin.readline

def star(n):
    if n==3:
        return ["  *  "," * * ","*****"]
    
    S=star(n//2)
    L=[]
    for i in S:
        L.append(" "*(n//2)  + i + " "*(n//2))
    for i in S:
        L.append(i + " " + i )
    return L 
    
n=int(input())
print("\n".join(star(n)))
