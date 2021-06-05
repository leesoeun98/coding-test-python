n, f = map(int, input().split())
res = [0 for i in range(n)]
#matrix 수학적으로 먼저 구하고
matrix = [1 for i in range(n)]
check = [0 for i in range(n + 1)]

for i in range(1, n):
    matrix[i] = matrix[i - 1] * (n - i) // i


def dfs(depth, sumnum):
    if depth == n and sumnum == f:
        print(*res)
        exit(0)
    else:
        #가지 n개 (1부터 n까지의 숫자로 구성됨)
        for i in range(1, n+1):
            if check[i]==0:
                res[depth]=i
                check[i]=1
                dfs(depth+1, sumnum+res[depth]*matrix[depth])
                check[i]=0
dfs(0,0)