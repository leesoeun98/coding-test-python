for t in range(int(input())):
    n, m = map(int, input().split())
    board=[]
    for i in range(n):
        arr=list(map(int, input().split()))
        board.append(arr)
    res=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sumv=0
            for k in range(m):
                for h in range(m):
                    sumv+=board[i+k][j+h]
            if res<sumv:
                res=sumv
    print("#"+str(t+1)+" "+str(res))
