import sys
input=sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
n,m=map(int,input().split())
parent=list(range(n))
cycle=False
for i in range(m):
    a,b=map(int,input().split())
    if cycle==True:
        continue
    if find(parent,a)==find(parent,b):
        print(i+1)
        cycle=True
    else:
        union(parent,a,b)
if cycle==False:
    print(0)
    
    