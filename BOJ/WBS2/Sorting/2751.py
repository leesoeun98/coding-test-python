import sys
#표준 입출력 사용시 시간초과
n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
for x in num:
    print(x)
