import sys
input=sys.stdin.readline

def perm(i,n,m,s,tmp):
    if i==m:
        print(" ".join(list(map(str,tmp))))
    else:
        for j in range(n):
            if i==0 or tmp[i-1]<=s[j]:
                tmp.append(s[j])
                perm(i+1,n,m,s,tmp)
                tmp.pop()
            
n,m=map(int,input().split())
s=sorted(list(map(int,input().split())))
result=[]

perm(0,n,m,s,[])

# from itertools import combinations_with_replacement

# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# N_list = sorted(N_list)

# for numbers in list(combinations_with_replacement(N_list, M)):
#     for num in numbers:
#         print(num, end=' ')
#     print()