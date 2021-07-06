import sys
num = [0] * (10001)
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    num[n] += 1
for i in range(len(num)):
    if num[i]!=0:
        for j in range(num[i]):
            print(i)
