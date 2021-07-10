n = int(input())
word={}
for _ in range(n):
    w = input()
    if w in word:
        word[w]+=1
    else:
        word[w]=1
for _ in range(n-1):
    w=input()
    if w in word:
        word[w]-=1
for key, value in word.items():
    if value!=0:
        print(key)