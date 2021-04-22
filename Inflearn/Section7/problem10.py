board = [list(map(int, input().split())) for i in range(7)]
check = [[0] * (7) for i in range(7)]
xd = [-1, 1, 0, 0]
yd = [0, 0, -1, 1]
count=0

def DFS(i, j):
    global count
    if i == 6 and j == 6:
        count+=1
        return
    else:
        for direction in range(4):
            nearx = i + xd[direction]
            neary = j + yd[direction]
            if 0 <= nearx <= 6 and 0 <= neary <= 6:
                if check[nearx][neary] == 0 and board[nearx][neary] == 0:
                    check[nearx][neary] = 1
                    DFS(nearx, neary)
                    check[nearx][neary]=0

check[0][0]=1
DFS(0, 0)
print(count)
