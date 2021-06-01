n = int(input())
score=list(map(int, input().split()))
avg=round(sum(score)/n)
index=1
beforeabs=abs(score[0]-avg)
beforescore=score[0]
for i in range(n):
    #beforeabs랑 현재 abs랑 비교해서 더 작은거로 갱신
    #만약 abs결과가 같다면 score로 비교
    #score도 같다면 i로 비교
    curabs=abs(score[i]-avg)
    if beforeabs>curabs:
        beforeabs=curabs
        index=i+1
        beforescore=score[i]
    elif beforeabs==curabs:
        if score[i]>beforescore:
            beforeabs = curabs
            index = i+1
            beforescore = score[i]
print(avg, index)

"""
n = int(input())
score=list(map(int, input().split()))
avg = round(sum(score)/n)
ans=[abs(score[0]-avg), score[0], 0]

for idx, s in enumerate(score):
    if abs(s-avg)<ans[0]:
        ans=[abs(s-avg), s, idx]
    elif abs(s-avg)==ans[0]:
        if s>ans[1]:
            ans = [abs(s - avg), s, idx]
        elif s==ans[1]:
            if idx<ans[2]:
                ans = [abs(s - avg), s, idx]
print(avg, ans[2]+1)

"""
