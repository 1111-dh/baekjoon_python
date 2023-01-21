import sys
input=sys.stdin.readline
answer=0
def backtrack(depth, n, chess):
    if depth==n:
        global answer
        answer+=1
    else:
        for i in range(n):
            chess[depth]=i
            flag=1
            for j in range(depth):
                if chess[depth]==chess[j] or abs(depth-j)==abs(chess[depth]-chess[j]) :
                    flag=0
                    break
            if flag==1:
                backtrack(depth+1,n,chess)

n=int(input())
backtrack(0,n,[0]*n)
print(answer)

