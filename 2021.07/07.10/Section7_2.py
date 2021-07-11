n = int(input())
meeting=[]
res=0
for _ in range(n):
    time, money = map(int, input().split())
    meeting.append([time, money])

def dfs(depth, price):
    global res
    if depth==n:
        if res<price:
            res=price
        return
    #넣고
    if depth+meeting[depth][0]<=n:
        dfs(depth+meeting[depth][0], price+meeting[depth][1])
    #안 넣고
    dfs(depth+1, price)

dfs(0,0)
print(res)