n, k = map(int, input().split())
score=[]
for _ in range(n):
    score.append(list(map(int, input().split())))
score.sort(key=lambda x:(-x[1], -x[2], -x[3]))
res=[]
before_gold=score[0][1]
before_silver=score[0][2]
before_bronze = score[0][3]
cnt=1
for i in range(n):
    if i==0:
        res.append([score[0][0], 1])
    else:
        before=res[-1][1]
        if before_gold==score[i][1] and before_silver==score[i][2] and before_bronze==score[i][3]:
            res.append([score[i][0], before])
            cnt=cnt+1
        else:
            res.append([score[i][0], before+cnt])
            cnt=1
            before_bronze=score[i][3]
            before_silver=score[i][2]
            before_gold=score[i][1]

for idx, s in res:
    if idx==k:
        print(s)
