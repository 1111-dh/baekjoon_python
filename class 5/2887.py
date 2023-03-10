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
nodes=[]
edges=[]
#[가중치,정점,정점]
for i in range(n):
    nodes.append(list(map(int,input().split()))+[i])
nodes.sort()#x기준
for i in range(n-1):
    edges.append([abs(nodes[i][0]-nodes[i+1][0]),nodes[i][-1],nodes[i+1][-1]])
nodes.sort(key=lambda x:x[1])#y기준
for i in range(n-1):
    edges.append([abs(nodes[i][1]-nodes[i+1][1]),nodes[i][-1],nodes[i+1][-1]])
nodes.sort(key=lambda x:x[2])#z기준
for i in range(n-1):
    edges.append([abs(nodes[i][2]-nodes[i+1][2]),nodes[i][-1],nodes[i+1][-1]])

edges.sort()
parent=list(range(n))
answer=0
for i in edges:
    w,a,b=i
    if find(parent,a)!=find(parent,b):
        union(parent,a,b)
        answer+=w
print(answer)