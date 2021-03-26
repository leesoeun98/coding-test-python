# 1차 시도 시간 초과
# 2차 시도 풀이 참고함
# 답이 특정 범위 내에 존재, 이때 이분 검색을 이용
k, n = map(int, input().split())
lan = [0 for _ in range(k)]
for i in range(k):
    lan[i] = int(input())
lan.sort()


def Count(x):
    count = 0
    for l in lan:
        count += (l // x)
    return count


left = 1
right = max(lan) - 1
res = 0
while left <= right and right < max(lan):
    mid = (left + right) // 2
    if Count(mid) >= n:
        # 랜선 길이 늘려서 개수 줄여야 함 => left 오른쪽으로 이동
        # 답의 후보가 여기에 존재..
        left = mid + 1
        res = mid
    else:
        right = mid - 1
print(res)
