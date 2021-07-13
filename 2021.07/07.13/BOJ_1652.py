n = int(input())
room=[list(input()) for _ in range(n)]
row, col=0, 0
#가로 검색
row_res=[]
for i in range(n):
    cnt=0
    for j in range(n):
        if room[i][j]=='.':
            cnt+=1
        else:
            if cnt>=2:
                row_res.append(cnt)
            cnt=0
    if cnt>=2:
        row_res.append(cnt)

#세로 검색
col_res=[]
for j in range(n):
    cnt=0
    for i in range(n):
        if room[i][j]=='.':
            cnt+=1
        else:
            if cnt>=2:
                col_res.append(cnt)
            cnt=0
    if cnt>=2:
        col_res.append(cnt)

print(len(row_res), len(col_res))
