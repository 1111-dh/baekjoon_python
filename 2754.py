sc={'0':0, '+':0.3, '-':-0.3}
ore={'A':4,'B':3,'C':2,'D':1}
ch=input()
if ch=='F': print(0.0)
else: print(float(sc[ch[1]]+ore[ch[0]]))