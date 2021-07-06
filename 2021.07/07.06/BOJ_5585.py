coins = [500, 100, 50, 10, 5, 1]
money=1000-int(input())
res=[]
for c in coins:
    res.append(money//c)
    money%=c
print(sum(res))