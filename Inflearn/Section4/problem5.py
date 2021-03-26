# 1차 시도 실패
# 2차 시도 답안 보고 함
n = int(input())
meeting = []
for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))
count = 0
endTime = 0
# 이전의 endTime과 지금의 start비교해서 endTime 먼저 끝나면 count
for start, end in meeting:
    if endTime <= start:
        count += 1
        endTime = end
print(count)