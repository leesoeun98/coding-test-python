code = list(map(str,input()))
dp=[1, 1]
if code[0]=='0':
    print(0)
    exit(0)
for i in range(1, len(code)):
    cnt=0
    if int(code[i])>0:
        cnt+=dp[-1]
    if 10<=int(''.join(code[i-1:i+1]))<=26:
        cnt+=dp[-2]
    dp.append(cnt%1000000)
print(dp[-1])
