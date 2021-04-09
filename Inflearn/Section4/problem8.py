#1차 시도 실패
#2차 시도 (답안 봄)
from collections import deque

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()
weight = deque(weight)
count = 0
while weight:
    if len(weight)==1:
        count+=1
        weight.pop()
    else:
        # 제일 무거운 사람, 가벼운 사람 못 타면 가장 무거운 사람만 태움
        if weight[0] + weight[-1] > m:
            count += 1
            weight.pop()
        else:
            # 둘다 태울 수 있으면 둘 다 태움
            count += 1
            weight.pop()
            weight.popleft()
print(count)
