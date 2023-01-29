import sys
input = sys.stdin.readline

n=int(input())
m=n
cnt=0
while True:
    m=(m//10 + m%10)%10 + m%10*10
    cnt+=1
    if m==n:
        print(cnt)
        break

# 문자열
# n=input().rstrip()
# m=n
# cnt=0
# while True:
#     if len(n)==1:
#         n='0'+n
#     n=n[-1]+str(int(n[0])+int(n[1]))[-1]
#     cnt+=1
#     if m==n:
#         break
# print(cnt)
    