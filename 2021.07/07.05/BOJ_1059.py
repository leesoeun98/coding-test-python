from itertools import combinations
l = int(input())
num = [0] + list(map(int, input().split()))
num.sort()
n = int(input())
cnt=0
if n in num:
    print(0)
    exit(0)

for idx in range(len(num)-1):
    start=num[idx]
    end=num[idx+1]
    if n in range(start, end):
        break

for temp in list(combinations(range(start+1, end), 2)):
    if n in range(temp[0], temp[1]+1):
        cnt+=1
print(cnt)
"""
for x in num:
    if n>x:
        left=x+1
    else:
        right=x-1
        break
print(right-left+(right-n)*(n-left))"""
