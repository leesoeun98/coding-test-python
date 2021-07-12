from itertools import combinations
n, m = map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
house=[]
pizza=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            house.append((i, j))
        if board[i][j]==2:
            pizza.append((i, j))

# pizza 집 중에서 m개 조합
pizza_distance=[]
for pizza_list in list(combinations(pizza, m)):
    # 각 집에서 피자집까지의 거리중 최소인게 피자거리
    distance=0
    for h in house:
        res=987654321
        for p in pizza_list:
            res=min(res, (abs(h[0]-p[0])+abs(h[1]-p[1])))
        distance+=res
    pizza_distance.append(distance)
print(min(pizza_distance))

