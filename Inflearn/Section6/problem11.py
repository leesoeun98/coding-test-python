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