n = int(input())
meeting=[]
for i in range(n):
    start, end=map(int, input().split())
    meeting.append((start, end))
#끝나는 시간 기준 정렬
meeting.sort(key=lambda x:(x[1], x[0]))
# 첫 회의 넣고 시작, 그래서 count=1부터 시작
count=1
endTime=meeting[0][1]
for m in meeting:
    if endTime<=m[0]:
        count+=1
        endTime=m[1]
print(count)