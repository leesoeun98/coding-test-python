n, k = map(int, input().split())
prince=[i for i in range(1, n+1)]

while prince:
    for _ in range(k-1):
        prince.append(prince.pop(0))
    prince.pop(0)
    if len(prince)==1:
        print(*prince)
        break