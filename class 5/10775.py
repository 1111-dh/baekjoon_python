import sys
input=sys.stdin.readline

def find(parent,x):
    if x!=parent[x]:
        parent[x]=find(parent,parent[x])
    return parent[x]

def union(parent,x,y):
    a=find(parent,x)
    b=find(parent,y)
    if a<b: parent[b]=a
    else: parent[a]=b
    
    
G=int(input())
P=int(input())
parent=list(range(G+1))
answer=0
flag=1
for _ in range(P):
    a=int(input())
    if flag:
        a=find(parent,a)
        if a==0:
            flag=0
            continue
        union(parent,a,a-1)
        answer+=1
print(answer)
