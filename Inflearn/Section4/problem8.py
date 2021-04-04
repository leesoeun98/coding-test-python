#1차 시도 실패
#2차 시도 (답안 봄)
from collections import deque
n, m = map(int, input().split())
weight=list(map(int, input().split()))
weight.sort()
count=0
p=deque(weight)
while p:
    if len(p)==1:
        count+=1
        p.pop()
        break
    # 2명 못 넣으면 젤 무거운 애 한명만 넣음
    if p[-1]+p[0]>m:
        count+=1
        p.pop()
    else:
        count+=1
        p.popleft()
        p.pop()
print(count)