import sys
input=sys.stdin.readline

dp=[]
now=''
n=int(input())

for _ in range(n):
    tmp=input().split()
    if tmp[0]=="type":
        now+=tmp[1]
        dp.append((int(tmp[-1]),now))
    else:
        ch,t=int(tmp[1]),int(tmp[-1])
        for i in range(len(dp)-1,-1,-1):
            if dp[i][0] < t - ch:
                now = dp[i][1]
                dp.append((t, now))
                break
        else:
            now = ''
            dp.append((t, now))
            
print(now)