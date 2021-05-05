n = int(input())
for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    for j in range((n - 1 - i) * 2):
        print(" ", end="")
    for j in range(i + 1):
        print("*", end="")
    print()
for i in range(1, n):
    for j in range(n - i, 0, -1):
        print("*", end="")
    for j in range(2 * i):
        print(" ", end="")
    for j in range(n - i, 0, -1):
        print("*", end="")
    print()
