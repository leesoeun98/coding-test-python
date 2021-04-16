k = int(input())
weight=list(map(int, input().split()))
res=set()
def DFS(depth, sumw):
    if depth==k:
        if 0<sumw<=sum(weight):
            res.add(sumw)
        return
    else:
        DFS(depth+1, sumw)
        DFS(depth+1, sumw-weight[depth]) #추를 오른쪽에
        DFS(depth+1, sumw+weight[depth]) #추를 왼쪽에
DFS(0, 0)
print(sum(weight)-len(res))