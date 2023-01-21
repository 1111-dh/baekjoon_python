import sys
while True:
    cnt=0
    try:
        s,t=sys.stdin.readline().split()
    except:
        break
    j=0
    for i in range(len(t)):
        if j>=len(s):
            break
        if t[i]==s[j]:
            j+=1
            cnt+=1
    if cnt==len(s):
        print("Yes")
    else:
        print("No")