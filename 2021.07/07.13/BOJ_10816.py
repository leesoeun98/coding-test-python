n = int(input())
card=list(map(int, input().split()))
m=int(input())
have=list(map(int, input().split()))
res=[0]*m
cards={}
for c in card:
    if c in cards:
        cards[c]+=1
    else:
        cards[c]=1

for i in range(m):
    if have[i] in cards:
        res[i]=cards[have[i]]
print(*res)