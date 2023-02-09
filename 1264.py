import sys
input=sys.stdin.readline
vowel=['a','e','i','o','u','A','E','I','O','U']
while True:
    string=input().rstrip()
    if string=="#": break
    
    cnt=0
    for i in string:
        if i in vowel:
            cnt+=1
    print(cnt)