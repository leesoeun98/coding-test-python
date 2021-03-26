# 1차 시도 실패
# 2차 시도 (답안 봄) 특히 count구하는 함수 (틀렸다가 다시 고침)
n, c = map(int, input().split())
stall = []
for _ in range(n):
    stall.append(int(input()))
# 마구간 좌표 오름차순
stall = sorted(stall)


# 말의 마리수 세기
def Count(distance):
    count = 1
    before = stall[0]
    # 이전 좌표와 현재 좌표의 차가 distance보다 크거나 같으면 성립되므로 count+=1
    for i in range(1, n):
        if stall[i] - before >= distance:
            count += 1
            before = stall[i]
    return count

# 말의 마리수가 c보다 크면 => 거리를 늘려야 함 => 정답도 이 안에 있음 + left를 오른쪽으로 이동
# 말의 마리수가 c보다 작으면 => 거리 줄여야 함 => right를 왼쪽으로 이동
left = 0
right = stall[n-1]
res = 0
while left <= right:
    mid = (left + right) // 2
    if Count(mid) >= c:
        res = mid
        left = mid + 1
    else:
        right = mid - 1
print(res)