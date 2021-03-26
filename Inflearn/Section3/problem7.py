import sys
n = int(input())
board=[]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
sum=0
s=e=n//2
"""
for i in range(n//2+1):
    for j in range(n//2-i, n//2+i+1):
        sum+=board[i][j]
for i in range(n//2+1, n):
    for j in range(n//2-(n-1-i), n//2+(n-1-i)+1):
        sum+=board[i][j]
"""
#7도 다시 보기
for i in range(n):
    for j in range(s, e+1):
        sum+=board[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(sum)