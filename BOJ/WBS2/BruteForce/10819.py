n = int(input())
num = list(map(int, input().split()))
res=0
def DFS(depth):
    global res
    if depth==n:
        sumnum=0
        for j in range(n-1):
            sumnum+=abs(num[j]-num[j+1])
        res=max(res, sumnum)
        return
    else:
        for i in range(depth, n):
            num[i], num[depth]= num[depth], num[i]
            DFS(depth+1)
            num[i], num[depth]= num[depth], num[i]
DFS(0)
print(res)