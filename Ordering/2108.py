from collections import Counter
import sys
n=int(sys.stdin.readline())
num=[]

for _ in range(n):
    num.append(int(sys.stdin.readline()))
#평균
avg=round(sum(num)/len(num), 0)

#중앙값
#정렬 필요
num=sorted(num)
mid=num[len(num)//2]

#최빈값 => Counter 사용
#정렬 필요
order=Counter(num).most_common()
if len(num)>1:
    if order[1][1]==order[0][1]:
        most=order[1][0]
    else:
        most=order[0][0]
else:
    most=order[0][0]
#범위
range=max(num)-min(num)

print("%d" %avg)
print(mid)
print(most)
print(range)