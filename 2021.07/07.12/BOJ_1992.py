n = int(input())
board=[list(map(int, input())) for _ in range(n)]

def decompose(x, y, n):
    if n==1:
        print(board[x][y], end="")
        return
    flag=True
    for i in range(x, x+n):
        if not flag:
            break
        for j in range(y, y+n):
            if board[x][y]!=board[i][j]:
                flag=False
                break
    if flag:
        print(board[x][y], end="")
    else:
        print("(", end="")
        decompose(x, y, n//2)
        decompose(x, y+n//2, n//2)
        decompose(x+n//2, y, n//2)
        decompose(x+n//2, y+n//2, n//2)
        print(")", end="")

decompose(0,0,n)