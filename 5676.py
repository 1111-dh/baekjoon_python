import sys
input=sys.stdin.readline

def set_tree(start,end,idx):
    if start==end:
        tree[idx]=arr[start]
        return arr[start]
    mid=(start+end)//2
    tree[idx]=set_tree(start,mid,idx*2)*set_tree(mid+1,end,idx*2+1)
    return tree[idx]

def interval_sum(start,end,idx,left,right):
    if start>right or end<left:
        return 1
    if start>=left and end<=right:
        return tree[idx]
    mid=(start+end)//2
    return interval_sum(start,mid,idx*2,left,right)*interval_sum(mid+1,end,idx*2+1,left,right)

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    if start == end:
        tree[index] = value
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = tree[index*2]*tree[index*2+1]

while True:
    try: n,k=map(int,input().split())
    except: break
    arr=list(map(int,input().split()))
    for i in range(n):
        if arr[i]>0: arr[i]=1
        elif arr[i]<0: arr[i]=-1
        else: arr[i]=0
    tree=[1]*4*n
    
    set_tree(0,n-1,1)
    answer=''
    for _ in range(k):
        a,b,c=input().split()
        b,c=int(b),int(c)
        if a=='C':
            if c>0: c=1
            elif c<0: c=-1
            update(0,n-1,1,b-1,c)
            arr[b-1]=c
        else:
            tmp=interval_sum(0,n-1,1,b-1,c-1)
            if tmp==-1: answer+='-'
            elif tmp==0: answer+='0'
            else: answer+='+'
    print(answer)
        
            