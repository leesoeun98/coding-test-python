# 1차 시도 실패
# 2차 시도 (답안 봄) 특히 count구하는 함수 (틀렸다가 다시 고침)
# 3차 시도 (답안 봄)

n,m = map(int, input().split())
stall=[]
for _ in range(n):
    stall.append(int(input()))
stall.sort()

# 마구간 개수 세기
def Count(distance):
    count=1
    before=stall[0]
    for i in range(1, n):
        if stall[i]-before>=distance:
            count+=1
            before=stall[i]
    return count

# 마구가 개수가 적을 때 => 거리 줄이고 마구간 개수 늘리기
# 마구간 개수가 많거나 같을 때 => 거리 늘리고 마구간 개수 줄이기
left=0
right=stall[-1]-stall[0]
answer=0
while left<=right:
    mid=(left+right)//2
    if Count(mid)<m:
        right=mid-1
    else:
        answer=mid
        left=mid+1
print(answer)