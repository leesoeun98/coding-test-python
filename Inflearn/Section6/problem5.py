c, n = map(int, input().split())
weight=[]
result=0

for i in range(n):
    weight.append(int(input()))

def DFS(depth, curweight):
    global result
    if curweight>c:
        return
    if depth==n:
        if result>curweight:
            result=curweight
        return
    else:
        DFS(depth+1, curweight+weight[depth])
        DFS(depth+1, curweight)
DFS(0,0)
print(result)