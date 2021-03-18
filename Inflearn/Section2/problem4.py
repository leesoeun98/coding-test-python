n = int(input())
score = list(map(int, input().split()))
avgscore=[]
minindex=-1
avg = round(sum(score) / n)
for s in score:
    avgscore.append(abs(s-avg))
for i in range(n):
    if min(avgscore)==avgscore[i]:
        minindex=i
        break
print(avg, minindex+1)