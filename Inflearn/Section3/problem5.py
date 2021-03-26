# 1차 시도 시간 초과
import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
count = 0
cont = 0
left = 0
right = 1
#값이 커지면 left 늘려서 수열을 줄이고, 값이 작아지면 right늘려서 수열 늘림
while left < right and right < n:
    cont = sum(num[left:right + 1])
    if cont == m:
        count += 1
        right += 1
    elif cont < m:
        right += 1
    elif cont > m:
        left += 1
print(count)
