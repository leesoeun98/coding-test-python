board=[list(map(int, input().split())) for i in range(9)]
# flag는 True로 시작
flag = True
for i in range(9):
    check1 = [0 for i in range(10)]
    check2 = [0 for i in range(10)]
    for j in range(9):
        if check1[board[i][j]]==0:
            check1[board[i][j]]+=1
        else:
            flag=False
            break
        if check2[board[j][i]]==0:
            check2[board[j][i]]+=1
        else:
            flag=False
            break
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        check = [0 for i in range(10)]
        for k in range(3):
            for h in range(3):
                if check[board[i+k][j+h]]==0:
                    check[board[i+k][j+h]]+=1
                else:
                    flag=False
                    break
if flag:
    print("YES")
else:
    print("NO")
