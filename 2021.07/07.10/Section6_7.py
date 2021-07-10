n = int(input())
coins=list(map(int, input().split()))
coins.sort(reverse=True)
m = int(input())
res=987654321
def dfs(cnt, money):
    global res
    if money>m:
        return
    if cnt>res:
        return
    if money==m and cnt<res:
        res=cnt
        return
    for i in range(n):
        dfs(cnt+1, money+coins[i])

dfs(0,0)
print(res)
