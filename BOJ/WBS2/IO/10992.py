n = int(input())
for i in range(1, n + 1):
    for j in range(n - i, 0, -1):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j == 1 or i == n or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
