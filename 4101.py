import sys
input = sys.stdin.readline

while True:
    a,b=map(int,input().split())
    if a==b==0: break
    print("YES" if a>b else "NO")