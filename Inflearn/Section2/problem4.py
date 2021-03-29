n = int(input())
score = list(map(int, input().split()))
avg = round(sum(score) / n)
smallest=[]
for idx, sc in enumerate(score):
    smallest.append((idx, abs(sc-avg)))
# abs 값 최소이면서 번호도 최소인게 [0] 원소
smallest.sort(key=lambda x: (x[1], x[0]))
print(avg, smallest[0][0]+1)
