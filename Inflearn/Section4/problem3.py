# 1차 시도 실패 (생각도 못함)
# 2차 시도 (답안 본 후 풀기) -> 답 틀림 
n, m = map(int, input().split())
album = list(map(int, input().split()))

def Count(mid):
    time=0
    count=1
    for a in album:
        if time+a> mid:
            time=a
            count+=1
        else:
            time+=a
    return count
left = 1
right = sum(album)
answer = 0
while left <= right:
    mid = (left + right) // 2  # 앨범 시간
    if Count(mid) >= m:
        left = mid + 1
    else:
        right = mid - 1
        answer=mid
# 1부터 sum(album)까지 시간 탐색
# 각 시간에 따른 앨범개수가 m개보다 크면 => 용량 늘리기, left를 오른쪽 이동
# 각 시간에 따른 앫범개수가 m개보다 작거나 같으면 => 용량 줄이기, right를 왼쪽 이동
print(answer)