n, m = map(int, input().split())
res=[0 for i in range(m)]
count=0
# 조합은 start하는 숫자가 1씩 증가해야 함
def DFS(depth, start):
    global count
    if depth==m:
        count+=1
        print(*res)
        return
    else:
        for i in range(start, n):
            res[depth]=i+1
            DFS(depth+1, i+1)

DFS(0,0)
print(count)