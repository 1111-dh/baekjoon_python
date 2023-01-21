import sys
input=sys.stdin.readline

def star(n):
    if n==3:
        return ["***","* *","***"]
    
    S=star(n//3)
    L=[]
    
    for i in S:
        L.append(i*3)
    for i in S:
        L.append(i + " "*(n//3) + i)
    for i in S:
        L.append(i*3)
    
    return L
    
n=int(input())
print("\n".join(star(n)))


# cnt=0
# def star(n,m,a):
#     if a==3:
#             print("***")
#             print("* *")
#             print("***")
#     elif n==3:
#         global cnt
#         cnt+=3
#         if a==m:
#             print("***"*(m//3))
#             print("* *"*(m//3))
#             print("***"*(m//3))
#         elif cnt>a//3 and cnt<=a-a//3:
#             if n==m:    #중앙
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("*"*(a//3),end="")
#                 print()
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("* *"+ " "*m + "* *",end="")
#                 print()
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("*"*(a//3),end="")
#                 print()
#             else:
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("*"*m,end="")
#                 print()
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("* *"*(m//3),end="")
#                 print()
#                 for i in range(3):
#                     if i==1:
#                         print(" "*(a//3),end="")
#                     else:
#                         print("*"*m,end="")
#                 print()
#         else:
#             for i in range(3):
#                 print("*"*(m//3) + " "*(m//3) + "*"*(m//3),end="")
#             print()
#             for i in range(3):
#                 print("* *"+ " "*(m//3) + "* *",end="")
#             print()
#             for i in range(3):
#                 print("*"*(m//3) + " "*(m//3) + "*"*(m//3),end="")
#             print()
#     else:
#         star(n//3,m,a)
#         star(n//3,m//3,a)
#         star(n//3,m,a)