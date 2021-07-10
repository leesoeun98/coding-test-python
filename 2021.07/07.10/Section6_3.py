n = int(input())
num=[i for i in range(1, n+1)]
def dfs(depth, visited):
    if depth==n:
        print(*visited)
    else:
        #넣고
        dfs(depth+1, visited+[num[depth]])
        #안 넣고
        dfs(depth+1, visited)

dfs(0,[])