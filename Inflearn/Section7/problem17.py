from itertools import combinations

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for i in range(n)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
pizza_store = []
house = []
total_distance = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            pizza_store.append((i, j))
        elif maps[i][j] == 1:
            house.append((i, j))
for l in list(combinations(pizza_store, m)):
    # per_combi 에는 각 집 당 피자집까지의 최소 거리 존재
    per_combi = []
    for xh, yh in house:
        per_distance_from_house = []
        for xp, yp in l:
            per_distance_from_house.append(abs(xh - xp) + abs(yh - yp))
        per_combi.append(min(per_distance_from_house))
    total_distance.append(sum(per_combi))
print(min(total_distance))
