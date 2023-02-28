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

V,E=map(int,input().split())
edges=[]
answer=0
for _ in range(E):
    edges.append(list(map(int,input().split())))
#(정점, 정점, 가중치)
edges.sort(key=lambda x : x[2])

parent=list(range(V+1))

for i in range(E):
    a,b,c=edges[i]
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        answer+=c
        
print(answer)
    


