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