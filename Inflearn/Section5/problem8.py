n =int(input())
readyword=[]
for _ in range(n):
    readyword.append(input())
for _ in range(n-1):
    readyword.remove(input())
print(*readyword)

"""
n =int(input())
readyword=[]
word=dict()
for _ in range(n):
    word[input()]=1
for _ in range(n-1):
    word[input()]=0
for key, value in word.items():
    if value==1:
        print(key)
        break
"""