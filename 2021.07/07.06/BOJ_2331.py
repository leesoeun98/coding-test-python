a, p = map(int, input().split())

def calc(num):
    numstr=list(str(num))
    sumnum=0
    for n in numstr:
        sumnum+=int(n)**p
    return sumnum

visited=[]
visited.append(a)
while True:
    cur=calc(visited[-1])
    if cur in visited:
        break
    visited.append(cur)
print(len(visited[:visited.index(calc(visited[-1]))]))