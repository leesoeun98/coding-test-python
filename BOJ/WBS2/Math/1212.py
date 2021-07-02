n = list(map(int, input()))
# 직접 계산 시 시간초과 남 => 8진수 1자리를 2진수 3자리로 바꾸기
o=["0","1","10","11","100","101","110","111"]
o2=["000","001","010","011","100","101","110","111"]
print(o[n[0]], end="")
for i in range(1, len(n)):
    print(o2[n[i]], end="")

"""
digit={0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
num=list(map(int, input()))
res=""
for n in num:
    res+=digit[n]
res=list(res)
while res and res[0]=='0':
    res.pop(0)
if len(res)==0:
    print(0)
else:
    print(''.join(res))
"""