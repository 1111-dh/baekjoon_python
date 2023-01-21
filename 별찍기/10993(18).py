import sys
input=sys.stdin.readline

def star(n):
    if n==1:
        return ["*"]
    S=star(n-1)
    L=[]
    index=0
    
    if n%2==0:
        space=(2**n-3)//2
        L.append("*" * (2**(n+1)-3))
        for i in range(1,2**n-2):
            if 0<i<=(2**n-1)//2:
                L.append(" "*i + "*" + " "*space + S[index] + " "*space + "*" + " "*i)
                index+=1
                space-=1
            else:
                space+=2
                L.append(" "*i + "*" + " "*((2**n-3)//2*2-space) + "*" + " "*i)
        L.append(" " * (2**n-2) + "*" + " " * (2**n-2))
    else:
        tmp=(2**(n+1)-3)//2
        space=0
        L.append(" " * tmp + "*" + " " * tmp)
        tmp-=1
        for i in range(1,2**n-2):
            if (2**n-1)//2 <= i < 2**n-2:
                L.append(" "*tmp + "*" + " "*space + S[index] + " "*space + "*" + " "*tmp)
                index+=1
                space+=1
            else:
                L.append(" "*tmp + "*" + " "*(2*i-1) + "*" + " "*tmp)
            tmp-=1
        L.append("*" * (2**(n+1)-3))
    return L

n=int(input())
N=star(n)
# sys.stdout = open('stdout.txt', 'w')
# print("\n".join(N))
if n%2:
    for i in range(2**n-1):
        for j in range(2**n-1+i):
            print(N[i][j],end="")
        print()
else:
    for i in range(2**n-1):
        for j in range(2**(n+1)-3-i):
            print(N[i][j],end="")
        print()

# sys.stdout.close()