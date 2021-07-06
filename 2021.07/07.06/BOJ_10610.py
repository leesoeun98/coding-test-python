num = list(input())
num.sort(reverse=True)
sumnum=0
for n in num:
    sumnum+=int(n)

if n[-1]=='0' and sumnum%3==0:
    print(''.join(num))
else:
    print(-1)