n, k = map(int, input().split())
line=[]
for _ in range(n):
    line.append(int(input()))

left=1
right=max(line)
res=0

def count(length):
    cnt=0
    for l in line:
        cnt+=l//length
    return cnt

while left<=right:
    mid=(left+right)//2
    #정답 포함
    if count(mid)>=k:
        res=mid
        left=mid+1
    else:
        right=mid-1
print(res)
