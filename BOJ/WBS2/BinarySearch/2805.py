n, m = map(int, input().split())
tree = list(map(int, input().split()))


def Count(height):
    total = 0
    for t in tree:
        if t >= height:
            total += (t - height)
    return total


left = 0
right = max(tree) + 1
answer = 0
while left <= right:
    mid = (left + right) // 2
    # 정답포함, 나무 높이 더 높여도 됨
    if Count(mid) >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)
