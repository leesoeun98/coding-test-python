k, n = map(int, input().split())
line = []
for _ in range(k):
    line.append(int(input()))


def Count(length):
    # 각 길이 당 만들 수 있는 랜선의 개수 반환하기
    count = 0
    for l in line:
        count += l // length
    return count


left = 1
# max값도 포함하기 위해 +1을 해야 함
right = max(line) + 1
answer = 0
while left <= right:
    mid = (left + right) // 2
    # 개수가 많으면 개수를 줄이고 길이를 늘려야 함 (정답 포함)
    if Count(mid) >= n:
        left = mid + 1
        answer = mid
    elif Count(mid) < n:
        # 개수 적으면 개수를 늘리고 길이 줄이기
        right = mid - 1
print(answer)
