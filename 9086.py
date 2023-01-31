import sys
input=sys.stdin.readline

for _ in range(int(input())):
    tmp=input().rstrip()
    print(tmp[0]+tmp[-1])