from collections import deque
n = list(map(int, input()))
n=deque(n)
dict={"000":0,"001":1,"010":2,"011":3,"100":4,"101":5,"110":6,"111":7}
#예외처리 꼼꼼히 무조건 else 쓰는거 x
if len(n)%3==1:
    n.appendleft(0)
    n.appendleft(0)
elif len(n)%3==2:
    n.appendleft(0)
n=list(n)
for i in range(0, len(n), 3):
    s=''.join(map(str, n[i:i+3]))
    print(dict.get(s), end="")

"""
digit={'000':0, '001':1, '010':2, '011':3, '100':4, '101':5, '110':6, '111':7}
num=list(input())
res=""
if len(num)%3==1:
    num=['0']+['0']+num
elif len(num)%3==2:
    num=['0']+num

for i in range(0,len(num), 3):
    res+=str(digit[''.join(num[i:i+3])])
print(res)"""