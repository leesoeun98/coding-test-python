n = int(input())
coins=[]
res=987654321
for _ in range(n):
    coins.append(int(input()))

def dfs(depth, suma, sumb, sumc):
    global res
    if depth==n:
        if suma!=sumb and suma!=sumc and sumb!=sumc:
            diff=max(suma, sumb, sumc)-min(suma, sumb, sumc)
            if res>diff:
                res=diff
        return
    #a에게
    dfs(depth+1, suma+coins[depth], sumb, sumc)
    #b에게
    dfs(depth+1, suma, sumb+coins[depth], sumc)
    #c에게
    dfs(depth+1, suma, sumb, sumc+coins[depth])

dfs(0,0,0,0)
print(res)
