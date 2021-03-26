# 1차 시도 시간 초과
# 2차 시도 풀이 참고함
k, n = map(int, input().split())
lan = [0 for _ in range(k)]
for i in range(k):
    lan[i] = int(input())
lan = sorted(lan)

def Count(len):
    count = 0
    for l in lan:
        count += (l // len)
    return count

left = 0
right = max(lan)
answer = 0
while left <= right and right < max(lan) + 1:
    mid = (left + right) // 2
    #최대길이 존재
    if Count(mid) >= n:
        left = mid + 1
        answer=mid
    #최소길이
    else:
        right = mid - 1
print(answer)
