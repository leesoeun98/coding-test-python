t = int(input())
k = int(input())
coins=[]
for _ in range(k):
    coins.append(list(map(int, input().split())))
cnt=0
def dfs(depth, price):
    global cnt
    if depth==k:
        if price==t:
            cnt+=1
        return
    if price>t:
        return
    else:
        for i in range(coins[depth][1]+1):
            dfs(depth+1, price+i*coins[depth][0])
dfs(0,0)
print(cnt)