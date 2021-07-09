k, n = map(int, input().split())
line=[]
for _ in range(k):
    line.append(int(input()))
def count(length):
    cnt=0
    for l in line:
        cnt+=l//length
    return cnt
left=1
right=max(line)
res=0
while left<=right:
    mid=(left+right)//2
    # 길이 줄이고 개수 늘리기
    if count(mid)<n:
        right=mid-1
    else:
        left=mid+1
        res=mid
print(res)