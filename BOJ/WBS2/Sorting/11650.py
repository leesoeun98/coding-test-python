# 표준입출력시 시간초과
import sys

n = int(sys.stdin.readline())
maps = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    maps.append((x, y))
maps.sort(key=lambda x: (x[0], x[1]))
for x, y in maps:
    print(x, y)
