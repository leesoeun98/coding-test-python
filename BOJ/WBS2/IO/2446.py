n = int(input())
for i in range(n, 0, -1):
    for j in range(n - i, 0, -1):
        print(" ", end="")
    for j in range(2 * i, 1, -1):
        print("*", end="")
    print()
for i in range(1, n):
    for j in range(n - i, 1, -1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
