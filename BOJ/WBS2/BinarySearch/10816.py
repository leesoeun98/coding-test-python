n = int(input())
have_card = list(map(int, input().split()))
m = int(input())
is_have = list(map(int, input().split()))

dic={}

for h in have_card:
    if h in dic:
        dic[h]+=1
    else:
        dic[h]=1
for h in is_have:
    if h in dic:
        print(dic[h], end=" ")
    else:
        print(0, end=" ")

"""
        have={}
n=int(input())
card=list(map(int, input().split()))
for c in card:
    if c in have:
        have[c]+=1
    else:
        have[c]=1
m=int(input())
check=[0]*m
query=list(map(int, input().split()))

for i in range(m):
    if query[i] in have:
        check[i]=have[query[i]]
    else:
        check[i]=0
print(*check)
"""