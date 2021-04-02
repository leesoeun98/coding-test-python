#1차 시도 실패
# 2차원 배열에서 열은 슬라이싱 불가
board = [0 for i in range(7)]
for i in range(7):
    board[i] = list(map(int, input().split()))
candidate=[]
count=0
#가로 회문 후보
for i in range(7):
    for j in range(3):
        temp = board[i][j:j+5]
        if temp==temp[::-1]:
            count+=1
        for k in range(2):
            if board[j+k][i]!=board[j+5-k-1][i]:
                break
        #for else 문
        else:
            count+=1

print(count)

"""
board=[list(map(int, input().split())) for _ in range(7)]
count=0
#가로 체크
for i in range(7):
    for j in range(3):
        for k in range(2):
            if board[i][j+k]!=board[i][j+4-k]:
                break
        else:
            count+=1
for i in range(7):
    for j in range(3):
        for k in range(2):
            if board[j+k][i]!=board[j+4-k][i]:
                break
        else:
            count+=1
print(count)
"""