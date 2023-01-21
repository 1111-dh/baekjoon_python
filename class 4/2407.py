import sys
from math import comb
n, m = map(int, sys.stdin.readline().split())
print(comb(n, m))