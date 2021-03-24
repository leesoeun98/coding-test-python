#1차 시도 시간 초과
import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
count = 0
for i in range(n):
    for j in range(i, n):
        if m == sum(num[i:j + 1]):
            count += 1
print(count)
