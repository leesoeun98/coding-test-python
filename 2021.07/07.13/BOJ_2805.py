n, m = map(int, input().split())
tree = list(map(int, input().split()))
def count(height):
    cnt=0
    for t in tree:
        if t>=height:
            cnt+=(t-height)
    return cnt

left=0
right=sum(tree)
res=0
while left<=right:
    mid=(left+right)//2
    if count(mid)>=m:
        res=mid
        left=mid+1
    else:
        right=mid-1
print(res)
