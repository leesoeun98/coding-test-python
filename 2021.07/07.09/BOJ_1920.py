n = int(input())
num=list(map(int, input().split()))
m = int(input())
isin=list(map(int, input().split()))
nums={}
for n in num:
    nums[n]=1

for i in range(m):
    if isin[i] in nums:
        print(1)
    else:
        print(0)