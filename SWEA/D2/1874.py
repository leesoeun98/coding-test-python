for t in range(1, int(input()) + 1):
    flag = True
    board = [list(map(int, input().split())) for i in range(9)]
    # 가로 체크
    for i in range(9):
        check = [0 for _ in range(10)]
        for j in range(9):
            if check[board[i][j]] == 0:
                check[board[i][j]] += 1
            else:
                flag = False
                break
    # 세로 체크
    for i in range(9):
        check = [0 for _ in range(10)]
        for j in range(9):
            if check[board[j][i]] == 0:
                check[board[j][i]] += 1
            else:
                flag = False
                break
    # 3*3 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0 for i in range(10)]
            for k in range(3):
                for h in range(3):
                    if check[board[j + k][i + h]] == 0:
                        check[board[j + k][i + h]] += 1
                    else:
                        flag = False
                        break
    if flag:
        print("#" + str(t) + " " + str(1))
    else:
        print("#" + str(t) + " " + str(0))
