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

n=int(input())
edges=[]
nodes=[]
for _ in range(n):
    nodes.append(list(map(float,input().split())))
for i in range(n):
    for j in range(n):
        if i<j:
            edges.append(list((((nodes[i][0]-nodes[j][0])**2+(nodes[i][1]-nodes[j][1])**2)**0.5,i,j)))
            #[가중치,노드,노드]
edges.sort()
parent=list(range(n))
answer=0
for i in edges:
    w,a,b=i
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        answer+=w
print(answer)


    


