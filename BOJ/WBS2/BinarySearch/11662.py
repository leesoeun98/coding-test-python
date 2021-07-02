import math

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
interval=10**6

adx=(bx-ax)/interval
ady=(by-ay)/interval
bdx=(dx-cx)/interval
bdy=(dy-cy)/interval

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2-x1, 2) +math.pow(y2-y1, 2))

mind = distance(ax, ay, cx, cy)
for i in range(1, interval+1):
    temp = distance(ax+adx*i, ay+ady*i, cx+bdx*i, cy+bdy*i)
    mind=min(temp, mind)
print(mind)