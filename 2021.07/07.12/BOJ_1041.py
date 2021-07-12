n = int(input())
dice = list(map(int, input().split()))
sumList = []
sumList.append(min(dice[0], dice[5]))
sumList.append(min(dice[1], dice[4]))
sumList.append(min(dice[2], dice[3]))
sumList.sort()
dice.sort()

res = 0
if n == 1:
    for i in range(5):
        res += dice[i]
else:
    blocks = [0, (n - 2) * (n - 2) + (n - 2) * (n - 1) * 4, 4 * (n - 1) + n * n - 4 - (n - 2) * (n - 2), 4]
    blocknums = [0, sumList[0], sumList[0] + sumList[1], sumList[0] + sumList[1] + sumList[2]]
    for i in range(4):
        res += blocknums[i] * blocks[i]
print(res)
