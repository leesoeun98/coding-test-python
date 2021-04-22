from collections import deque

start, end = map(int, input().split())
maps = [0] * 10001
count = [0] * 10001
check = [0] * 10001
queue = deque()
# 초기화
queue.append(start)
check[start] = 1
count[start] = 0
while (queue):
    cur = queue.popleft()
    if cur == end:
        break
    for next in (cur - 1, cur + 1, cur + 5):
        # 범위 주의
        if 0 < next <= 10000:
            if check[next] == 0:
                check[next] = 1
                count[next] = count[cur] + 1
                queue.append(next)
print(count[end])
