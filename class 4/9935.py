import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()

stack = []
length = len(b)

for i in a:
    stack.append(i)
    if i == b[-1] and ''.join(stack[-length:]) == b:
        del stack[-length:]
        
answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)

