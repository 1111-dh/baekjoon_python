import sys
input=sys.stdin.readline

# 재귀로 마지막 숫자만
# def josephus(n, k):
#     if n ==1:
#         return 1
#     else:
#         return ((josephus(n-1,k)+k-1)%n)+1
# n,k=map(int,input().split())
# print(josephus(n,k))

# 큐 이용
# from collections import deque
# n,k=map(int,input().split())
# print("<",end="")
# lst=deque(range(1,n+1))
# cnt=0
# while len(lst)>1:
#     cnt+=1
#     if cnt%k:
#         lst.append(lst.popleft())
#     else:
#         print(lst.popleft(),end=", ")
# print(lst[0],end=">")


# 수학 계산
# n,k=map(int,input().split())
# print("<",end="")
# j=0
# lst=list(range(1,n+1))
# for i in range(1,n):
#     j=(j+k-1)%len(lst)
#     print(lst.pop(j),end=", ")
# print(lst[0],end=">")