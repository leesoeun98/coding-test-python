a, p = map(int, input().split())
temp = [a]
duplicate = 0
while True:
    before = temp[-1]
    cur = 0
    while before > 0:
        cur += pow(before % 10, p)
        before //= 10
    # 종료 조건
    if cur in temp:
        duplicate=cur
        break
    else:
        temp.append(cur)
count=0
for t in temp:
    if t!=duplicate:
        count+=1
    else:
        break
print(count)
"""
a, p = map(int, input().split())
cycle=[]
def calc(num):
    nu=list(str(num))
    res=0
    for n in nu:
        res+=int(n)**p
    return res

cycle.append(a)
while True:
    before=cycle[-1]
    cur=calc(before)

    if cur in cycle:
        break
    else:
        cycle.append(cur)
rest=cycle[:cycle.index(calc(cycle[-1]))]
print(len(rest))"""