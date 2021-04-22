n, k = map(int, input().split())
num=list(map(int, input().split()))
m= int(input())
count=0
def DFS(depth, start, sum):
    global count
    if depth==k:
        if sum%m==0:
            count+=1
        return
    else:
        for i in range(start, n):
            DFS(depth+1, i+1, sum+num[i])
DFS(0,0, 0)
print(count)

"""
n, k = map(int, input().split())
num=list(map(int, input().split()))
res=[0 for i in range(k)]
m = int(input())
count=0
def DFS(depth, start):
    global count
    if depth==k:
        if sum(res) %m==0:
            count+=1
        return
    else:
        for i in range(start, n):
            res[depth]=num[i]
            DFS(depth+1, i+1)
DFS(0,0)
print(count)
"""