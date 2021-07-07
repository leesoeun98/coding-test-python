n=int(input())
paper=[list(map(int, input().split())) for _ in range(n)]
answer=[0,0,0]

def decompose(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j]!=paper[x][y]:
                for k in range(3):
                    for l in range(3):
                        decompose(x+k*n//3, y+l*n//3, n//3)
                return

    if paper[x][y]==-1:
        answer[0]+=1
    elif paper[x][y]==0:
        answer[1]+=1
    else:
        answer[2]+=1
decompose(0,0,n)
for a in answer:
    print(a)
