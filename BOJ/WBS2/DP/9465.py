for t in range(int(input())):
    n = int(input())
    sticker=[]
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    sticker[0][1] += sticker[1][0]
    sticker[1][1] += sticker[0][0]
    for j in range(2, n):
        sticker[0][j] += max(sticker[1][j - 1], sticker[1][j - 2])
        sticker[1][j] += max(sticker[0][j - 1], sticker[0][j - 2])
    print(max(sticker[0][n - 1], sticker[1][n - 1]))
