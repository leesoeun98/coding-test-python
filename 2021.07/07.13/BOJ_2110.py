n, c = map(int, input().split())
house=[]
for _ in range(n):
    house.append(int(input()))
house.sort()

def count(distance):
    cnt=1
    before=house[0]
    for i in range(1, n):
        if house[i]-before>=distance:
            cnt+=1
            before=house[i]
    return cnt

left=house[0]
right=house[-1]
res=0
while left<=right:
    mid = (left+right)//2
    if count(mid)>=c:
        left=mid+1
        res=mid
    else:
        right=mid-1
print(res)
