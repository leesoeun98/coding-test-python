dots=[]
xd=[]
yd=[]
for _ in range(3):
    #미리 저장시키기
    dots.append(list(map(int, input().split())))

for x, y in dots:
    #각 원소에 대해서 있으면 remove, 없으면 append
    if x in xd:
        xd.remove(x)
    else:
        xd.append(x)
    if y in yd:
        yd.remove(y)
    else:
        yd.append(y)
print(xd[0], yd[0])