from itertools import combinations

l = int(input())
num=[0]+list(map(int, input().split()))
num.sort()
n = int(input())

cnt=0
for i in range(l):
    start=num[i]
    end=num[i+1]
    if n in range(start, end):
        break
for temp in list(combinations(range(start+1, end), 2)):
    if n in range(temp[0], temp[1]+1):
        cnt+=1
print(cnt)