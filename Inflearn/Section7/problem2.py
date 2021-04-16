n = int(input())
schedule=[]
result=-987654321
for _ in range(n):
    time, money = map(int, input().split())
    schedule.append((time, money))
def DFS(depth, money):
    global result
    if depth==n:
        if money>=result:
            result=money
        return
    else:
        #상담 할 때
        if depth+schedule[depth][0]<=n:
            DFS(depth+schedule[depth][0],money+schedule[depth][1])
        #상담 안할 때 +1 하는거 잊지 말기
        DFS(depth+1, money)
DFS(0,0)
print(result)