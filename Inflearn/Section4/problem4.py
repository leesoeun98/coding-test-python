# 1차 시도 실패
# 2차 시도 (답안 봄) 특히 count구하는 함수 (틀렸다가 다시 고침)
# 3차 시도 (답안 봄)

n, c = map(int, input().split())
stall=[]
for i in range(n):
    stall.append(int(input()))
stall.sort()
def Count(distance):
    count=1
    before=stall[0]
    for i in range(1, n):
        if stall[i]-before>=distance:
            count+=1
            before=stall[i]
    return count

# 말의 수가 c보다 많으면 (정답 포함) => 말의 수 줄이고 거리 늘리고
# 말의 수가 c보다 적으면 => 말의 수 늘리고 거리 줄이고
left=1
right=stall[-1]
res=0
while left<=right:
    mid=(left+right)//2
    if Count(mid)>=c:
        res=mid
        left=mid+1
    else:
        right=mid-1
print(res)
