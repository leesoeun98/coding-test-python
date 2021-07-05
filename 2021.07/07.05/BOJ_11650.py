n = int(input())
board=[]
for _ in range(n):
    x, y = map(int, input().split())
    board.append((x, y))
board.sort(key=lambda x:(x[0], x[1]))
for x, y in board:
    print(x, y)