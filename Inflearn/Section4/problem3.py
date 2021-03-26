# 1차 시도 실패 (생각도 못함)
# 2차 시도 (답안 본 후 풀기) -> 답 틀림
# 3차 시도 (답안 본건데도 틀림) -> 3차 때 이해함

n, m = map(int, input().split())
album = list(map(int, input().split()))


# 각 용량당 앨범개수 구해서, m개보다 개수가 많으면 => 용량 늘리기 left 오른쪽 이동
# 각 용량당 앨범개수 구해서, m개보다 개수가 적으면 => 용량 줄이기 right 왼쪽 이동

# 각 용량당 앨범개수 구하는 함수
def Count(capacity):
    time = 0
    count = 1
    for a in album:
        if time + a > capacity:
            time = a
            count += 1
        else:
            time += a
    return count


left = 1
right = sum(album)
while left <= right:
    mid = (left + right) // 2
    # 앨범 당 용량이 어떤 노래보다도 커야 함 (즉, 가장 큰 노래보다 각 용량이 더 커야 함)
    if mid >= max(album) and Count(mid) <= m:
        # 앨범 개수 적게 가능하면 당연히 가능 그래서 정답이 여기에 있음
        right = mid - 1
        res = mid
    else:
        left = mid + 1
print(res)
