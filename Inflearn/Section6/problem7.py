n = int(input())
coins=list(map(int, input().split()))
coins.sort(reverse=True)
change=int(input())
def DFS(change, result):
    if change==0:
        print(result)
        return
    else:
        for i in range(n):
            #coin 넣었을 때
            DFS(change%coins[i], result+change//coins[i])
DFS(change, 0)