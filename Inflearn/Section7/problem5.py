"""n = int(input())
coins = []
for _ in range(n):
    coins.append(int(input()))
res=987654321

def DFS(depth, sum1, sum2, sum3):
    global res
    if depth == n:
        if sum1 != sum2 and sum1 != sum3 and sum2 != sum3:
            diff=abs(max(sum1, sum2, sum3)-min(sum1, sum2, sum3))
            if diff<res:
                res=diff
        return
    else:
        # 1번에게 준다
        DFS(depth + 1, sum1 + coins[depth], sum2, sum3)
        DFS(depth + 1, sum1, sum2 + coins[depth], sum3)
        DFS(depth + 1, sum1, sum2, sum3 + coins[depth])


DFS(0, 0, 0, 0)
print(res)"""
n=int(input())
money=[0]*3
coins = []
for _ in range(n):
    coins.append(int(input()))
res=987654321

def DFS(depth):
    global res
    if depth==n:
        diff=max(money)-min(money)
        if diff<res:
            tmp=set()
            for m in money:
                tmp.add(m)
            if len(tmp)==3:
                res=diff
        return
    else:
        for i in range(3):
            money[i]+=coins[depth]
            DFS(depth+1)
            #원상복귀
            money[i]-=coins[depth]
DFS(0)
print(res)