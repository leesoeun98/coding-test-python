n = int(input())
meeting=[]
for i in range(n):
    start, end=map(int, input().split())
    meeting.append((start, end))
#끝나는 시간 기준 정렬
meeting.sort(key=lambda x:(x[1], x[0]))
#첫 회의는 무조건 들어가야 함 그래서 endTime은 0부터 시작
endTime=0
count=0
for start, end in meeting:
    if endTime<=start:
        count+=1
        endTime=end
print(count)