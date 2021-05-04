for t in range(int(input())):
    n=int(input())
    res=[[1]]
    for i in range(1, n):
        row=[1]
        for j in range(len(res[-1])-1):
            sumv=res[-1][j]+res[-1][j+1]
            row.append(sumv)
        row.append(1)
        res.append(row)
    print("#" + str(t + 1))
    for r in res:
        print(*r)