import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()
len_a=len(a)
len_b=len(b)

answer=[0]*len_a
string=['']*len_a
for i in range(len_b):
    cnt=0
    tmp=''
    for j in range(len_a):
        if cnt<answer[j]:
            cnt=answer[j]
            tmp=string[j]
        elif b[i]==a[j]:
            answer[j]=cnt+1
            string[j]=tmp+a[j]
max_len=0
max_str=''
for i in range(len_a):
    if max_len<answer[i]:
        max_len=answer[i]
        max_str=string[i]
print(max_len)
print(max_str)

