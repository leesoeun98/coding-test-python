n = int(input())
have_card = list(map(int, input().split()))
m = int(input())
is_have = list(map(int, input().split()))
# 정렬 주의
have_card.sort()

#각 i 당 이분탐색하기
for i in is_have:
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if i==have_card[mid]:
            print(1, end=" ")
            break
        elif have_card[mid]<i:
            left=mid+1
        else:
            right=mid-1
        if left>right:
            print(0,end=" ")
            break