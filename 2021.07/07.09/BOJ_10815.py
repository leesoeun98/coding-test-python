n = int(input())
card=list(map(int, input().split()))
m = int(input())
isin=list(map(int, input().split()))

res=[0]*m
cards={}
for c in card:
    cards[c]=1

for i in range(m):
    if isin[i] in cards:
        res[i]=1
    else:
        res[i]=0
print(*res)