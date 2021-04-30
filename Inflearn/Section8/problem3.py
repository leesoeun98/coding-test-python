n = int(input())
res=[0]*(n+1)
def DFS(depth):
    if res[depth]>0:
        return res[depth]
    if depth==1 or depth==2:
        return depth
    else:
        return DFS(depth-1)+DFS(depth-2)
print(DFS(n))