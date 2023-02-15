import sys
import math
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

a,b=map(int,input().split())


def solve(x):
    if x<=0:
        return 0
    seung = int(math.log2(x))
    floor=2**seung
    if floor==x:
        return seung * x // 2 + 1
    dif=x-floor
    return solve(floor) + dif + solve(dif)

print(solve(b)-solve(a-1))