from itertools import combinations
height = []
for _ in range(9):
    height.append(int(input()))

for lst in list(combinations(height, 7)):
    if sum(lst)==100:
        temp=list(lst)
        temp.sort()
        for t in temp:
            print(t)
        break
