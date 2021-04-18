from collections import deque
n, k = map(int, input().split())
prince=[i for i in range(1, n+1)]
prince=deque(prince)
while prince:
    if len(prince)==1:
        print(*prince)
        break
    for i in range(k-1):
        prince.append(prince.popleft())
    prince.popleft()
