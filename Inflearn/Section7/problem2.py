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

"""
n = int(input())
schedule=[]
for i in range(n):
    day, money=map(int, input().split())
    schedule.append((day, money))
res=0
def DFS(depth, summ):
    global res
    #n일 다 되면 끝
    if depth>=n:
        if res<summ and depth==n:
            res=summ
        return
    else:
        #상담 하기
        DFS(depth+schedule[depth][0], summ+schedule[depth][1])
        #상담 안하기
        DFS(depth+1, summ)
DFS(0,0)
print(res)
"""