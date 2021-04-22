t = int(input())
k = int(input())
coin = []
for i in range(k):
    value, count = map(int, input().split())
    coin.append((value, count))
count = 0


def DFS(depth, sumc):
    global count
    if depth == k:
        if sumc == t:
            count += 1
        return
    if sumc > t:
        return
    else:
        for i in range(coin[depth][1] + 1):
            # 동전마다 개수가 다른데, 각 동전의 type이 depth가 되고 동전의 개수가 가지가 됨
            DFS(depth + 1, sumc + coin[depth][0] * i)


DFS(0, 0)
print(count)
