def check(x):
    flag = True
    for i in range(len(x) // 2):
        if x[i] != x[- i - 1]:
            flag = False
            return flag
    return flag

n = int(input())

for _ in range(n):
    word = input().lower()
    if word==word[::-1]:
        print("YES")
    else:
        print("NO")

"""
n = int(input())
for _ in range(n):
    word=input().lower()
    for i in range(len(word)//2):
        if word[0+i]!=word[len(word)-1-i]:
            print("NO")
            break
    else:
        print("YES")
"""