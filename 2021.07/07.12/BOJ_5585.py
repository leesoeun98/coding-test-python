coins=[500,100,50,10,5,1]
m=int(input())
res=0
money=1000-m
for i in range(len(coins)):
    res+=money//coins[i]
    money%=coins[i]
print(res)