ladder = [list(map(int, input().split())) for i in range(10)]
check = [[0] * 10 for _ in range(10)]


# 거꾸로 탐색 => 사다리 올라거나 (위로), 왼 오
#단, 이때 위로 계속 올라갈 수 있으니 위로 가기 전에 왼 / 오 먼저 탐색해야 함
def dfs(i, j):
    check[i][j] = 1
    if i == 0:
        print(j)
    else:
        if j - 1 >= 0 and ladder[i][j - 1] == 1 and check[i][j - 1] == 0:
            dfs(i, j - 1)
        elif j + 1 < 10 and ladder[i][j + 1] == 1 and check[i][j + 1] == 0:
            dfs(i, j + 1)
        else:
            dfs(i-1, j)


for i in range(10):
    if ladder[9][i] == 2:
        dfs(9, i)