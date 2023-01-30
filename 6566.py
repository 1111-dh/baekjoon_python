import collections
 
anagrams = collections.defaultdict(list)
li = []
tmp = []
 
while True:
    try:
        word = input()
        li.append(word)
    except EOFError:
        break
 
for i in li:
    anagrams["".join(sorted(i))].append(i)
 
max_len = -1
for i in anagrams.keys():
    sorted_anagram = sorted(anagrams[i])
    max_len = max(max_len, len(sorted_anagram))
    tmp.append(sorted_anagram)
tmp.sort(key=lambda x: (max_len - len(x), x[0]))
for i in range(min(len(tmp), 5)):
    print(f'Group of size {len(tmp[i])}: {" ".join([elem for elem in sorted(list(set(tmp[i])))])} .')
    

# import sys
# input=sys.stdin.readline

# dic=dict()
# while True:
#     try:
#         tmp=input().rstrip()
#     except EOFError:
#         break
#     temp="".join(sorted(list(tmp)))
#     if temp in dic:
#         dic[temp].append(tmp)
#     else:
#         dic[temp]=[tmp]
# for i in dic:
#     dic[i]=list(set(dic[i]))
# dic=sorted(list(map(sorted,dic.values())),key=lambda x: (-len(x),x))
# cnt=0
# for i in range(5):
#     print("Group of size %d: "%len(dic[i]),end="")
#     print(" ".join(dic[i]),end=" .\n")