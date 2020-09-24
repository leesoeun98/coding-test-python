n, m=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(list(input())))

mincount=64
def WB(i, j):#시작이 W라면
    count=0
    for k in range(i, i+8):
        for h in range(j, j+8):
            #8*8모두 반복해서 돌기
            if k%2==1 and h%2==0:
                #각 행과 열의 짝, 홀수 자리에 b가 위치하는지 확인
                if board[k][h]=='W':
                    count+=1
            elif k%2==0 and h%2==0:
                if board[k][h]=='B':
                    count+=1
            elif k%2==0 and h%2==1:
                if board[k][h]=='W':
                    count+=1
            elif k%2==1 and h%2==1:
                if board[k][h]=='B':
                    count+=1
    return count

def BW(i, j):
    count=0
    for k in range(i, i+8):
        for h in range(j, j+8):
            if k%2==1 and h%2==0:
                if board[k][h]=='B':
                    count+=1
            elif k%2==0 and h%2==0:
                if board[k][h]=='W':
                    count+=1
            elif k%2==0 and h%2==1:
                if board[k][h]=='B':
                    count+=1
            elif k%2==1 and h%2==1:
                if board[k][h]=='W':
                    count+=1
    return count

for i in range(n-7):
    for j in range(m-7):
        #8*8짜리 체스판 읽어오기위해서 각 행과 열의 길이에서 7빼
        mincount=min(mincount, WB(i, j), BW(i, j))

print(mincount)