board = [0 for i in range(9)]
for i in range(9):
    board[i] = list(map(int, input().split()))

# 가로 체크
for i in range(9):
    check = [0 for i in range(10)]
    for j in range(9):
        if check[board[i][j]] == 0:
            check[board[i][j]] += 1
        else:
            print("NO")
            exit(0)
# 세로 체크
for i in range(9):
    check = [0 for i in range(10)]
    for j in range(9):
        if check[board[j][i]] == 0:
            check[board[j][i]] += 1
        else:
            print("NO")
            exit(0)

# 3*3 체크
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        check = [0 for i in range(10)]
        for row in range(3):
            for col in range(3):
                if check[board[i+row][j+col]] == 0:
                    check[board[i+row][j+col]] += 1
                else:
                    print("NO")
                    exit(0)
print("YES")

"""
# check 별도로 두는거 잊지 말기
board=[list(map(int, input().split())) for _ in range(9)]

# 가로, 세로 체크
for i in range(9):
    check1=[0 for _ in range(10)]
    check2=[0 for _ in range(10)]
    for j in range(9):
        if check1[board[i][j]]==0:
            check1[board[i][j]]+=1
        else:
            print("NO")
            exit(0)
        if check2[board[j][i]]==0:
            check2[board[j][i]]+=1
        else:
            print("NO")
            exit(0)
# 각 칸 체크
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        check=[0 for _ in range(10)]
        for k in range(3):
            for h in range(3):
                if check[board[i+k][j+h]]==0:
                    check[board[i + k][j + h]]+=1
                else:
                    print("NO")
                    exit(0)
print("YES")

"""