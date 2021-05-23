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
