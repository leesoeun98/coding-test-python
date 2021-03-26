# 1차 시도 실패
# 2차 시도 답안 보고 함
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))
count = 0
endTime = 0
# 다음 end와 비교해야하므로 endTime 변수를 둠
for start, end in meeting:
    if endTime <= start:
        endTime = end
        count += 1
print(count)
