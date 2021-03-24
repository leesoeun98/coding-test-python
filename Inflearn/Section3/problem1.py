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
