for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    board=[list(map(int, input().split())) for i in range(n)]
    res=0
    #가로 탐색
    for col in range(n):
        cnt=row=0
        while True:
            if board[col][row]==1:
                cnt+=1
                row+=1
            else:
                if cnt==k:
                    res+=1
                cnt=0
                row+=1
            if row==n:
                if cnt==k:
                    res+=1
                break
    #세로 탐색
    for row in range(n):
        cnt=col=0
        while True:
            if board[col][row]==1:
                cnt+=1
                col+=1
            else:
                if cnt==k:
                    res+=1
                cnt=0
                col+=1
            if col==n:
                if k==cnt:
                    res+=1
                break
    print("#"+str(t)+" "+str(res))







