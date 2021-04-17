first=input()
second=input()
check1=[0 for i in range(52)]
check2=[0 for i in range(52)]
flag=True
for f in first:
    if f.islower():
        check1[ord(f)-ord('a')+26]+=1
    else:
        check1[ord(f)-ord('A')]+=1
for s in second:
    if s.islower():
        check2[ord(s)-ord('a')+26]+=1
    else:
        check2[ord(s)-ord('A')]+=1
for i in range(52):
    if check2[i]==check1[i]:
        flag=True
    else:
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")
"""
first=input()
second=input()
word=dict()
for f in first:
    word[f]=word.get(f, 0)+1
for s in second:
    word[s]=word.get(s, 0)-1
for key, value in word.items():
    if value!=0:
        print("NO")
        break
else:
    print("YES")
"""