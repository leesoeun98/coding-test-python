num = input()
num=sorted(num, reverse=True)
sumnum=0
for n in num:
    sumnum+=int(n)
if sumnum%3==0 and num[-1]=='0':
    print(''.join(num))
else:
    print(-1)