#1차 시도 실패
n = int(input())
number = list(map(int, input().split()))
answer = [float("inf") for _ in range(n+1)]
for i in range(1, n+1):
    idx = 0
    while idx != number[i-1]:
        if i < answer[idx]:
            idx += 1
        else:
            continue
    answer[idx] = i
print(*answer)
