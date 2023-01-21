import sys
from collections import deque
input=sys.stdin.readline

n,k=map(int,input().split())
visit=[0]*100001
m=99999999
cnt=0
que=deque()
que.append(n)
while que:
    node=que.popleft()
    if visit[node]<=m:
        if node == k:
            if visit[node]==m:
                cnt+=1
            elif visit[node]<m:
                m=visit[node]
                cnt=1
        else:
            for i in (node+1,node-1,node*2):
                if 0<=i<=100000 and (visit[i]==0 or visit[i]==visit[node]+1):
                    visit[i]=visit[node]+1
                    que.append(i)
        
print(m)
print(cnt)
        