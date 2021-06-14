code=list(map(str, input()))
if code[0]=='0':
    print(0)
    exit(0)

dp=[1,1]
mod=1000000

# 각 i가 코드의 마지막이라고 가정
# -> 각 i번째 일때 i-1, i 합쳐진걸로 판별
for i in range(1, len(code)):
    cnt=0
    cur=int(''.join(code[i-1:i+1]))
    if int(code[i])>0:
        cnt+=dp[-1]
    if cur>=10 and cur<=26:
        cnt+=dp[-2]
    dp.append(cnt%mod)

print(dp[-1])
