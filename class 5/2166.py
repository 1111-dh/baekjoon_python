n=int(input())

x,y=[],[]
s=0

for _ in range(n):
    _x,_y=map(int,input().split())
    x.append(_x)
    y.append(_y)
    
for i in range(n):
    s+=(x[i]*y[(i+1)%n]-y[i]*x[(i+1)%n])/2
    
print(round(abs(s),1))