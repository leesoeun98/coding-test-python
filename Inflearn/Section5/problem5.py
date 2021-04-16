#1차 시도 실패 (답안 봄)
from collections import deque
n, k = map(int, input().split())
prince=[i for i in range(1, n+1)]
prince=deque(prince)
while prince:
    for _ in range(k-1):
        p=prince.popleft()
        prince.append(p)
    prince.popleft()
    if len(prince)==1:
        print(prince[0])
        prince.popleft()

"""
from collections import deque
n, k = map(int, input().split())
prince=[i for i in range(1, n+1)]
prince=deque(prince)
while len(prince)>1:
    before=[]
    for i in range(k-1):
            prince.append(prince.popleft())
    prince.popleft()
print(*prince)
"""