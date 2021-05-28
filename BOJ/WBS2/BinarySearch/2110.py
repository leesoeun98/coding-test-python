n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()


def Count(distance):
    # 최대 거리가 distance일 때 공유기 개수 반환하는 함수
    # 첫번째에 넣을거라 count는 1부터 시작
    before = house[0]
    count = 1
    for i in range(1, len(house)):
        if house[i] - before >= distance:
            count += 1
            before = house[i]
    return count


left = 1
right = house[-1]
answer = 0
while left <= right:
    mid = (left + right) // 2
    # 공유기 개수가 많으면 개수 줄이고 거리 늘리기 가능
    # 정답 포함
    if Count(mid) >= c:
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)
