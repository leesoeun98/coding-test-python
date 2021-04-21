n=int(input())
check=[0 for i in range(n)]
def DFS(depth):
    if depth==n:
        for i in range(n):
            if check[i]==1:
                print(i+1, end="")
        print()
        return
    else:
        #넣고
        check[depth]=1
        DFS(depth+1)
        #안 넣고
        check[depth]=0
        DFS(depth+1)
DFS(0)
