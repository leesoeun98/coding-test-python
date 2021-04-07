n = int(input())
word=[]
used=[]
for i in range(n):
    word.append(input())
for i in range(n-1):
    used=input()
    if used in word:
        word.remove(used)
print(*word)