n, m = map(int, input().split())
res=[0 for i in range(m)]
count=0
def DFS(depth):
    global count
    if depth==m:
        count+=1
        print(*res)
        return
    else:
        # 가지가 n개이므로 for 문 사용
        for i in range(1, n+1):
            res[depth]=i
            DFS(depth+1)
DFS(0)
print(count)