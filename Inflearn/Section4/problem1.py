def binarySearch(x):
    left = 0
    right = n - 1
    # left<=right 임에 주의
    while left <= right and right < n:
        mid = (left + right) // 2
        if x == num[mid]:
            return mid + 1
        elif x > num[mid]:
            left = mid + 1
        else:
            right = mid - 1


n, m = map(int, input().split())
num = list(map(int, input().split()))
num = sorted(num)
print(binarySearch(m))
"""
n, m = map(int, input().split())
num=list(map(int, input().split()))
num.sort()
left=0
right=n-1
res=0
while left<=right:
    mid=(left+right)//2
    if num[mid]==m:
        res=mid+1
        break
    elif num[mid]>m:
        right=mid-1
    else:
        left=mid+1
print(res)
"""