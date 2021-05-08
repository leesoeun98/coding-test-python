d1, d2, d3 = map(int, input().split())
a = round((d2 + d1 - d3) / 2, 1)
b = d1 - a
c = d3 - b
if 0 < a and 0 < b and 0 < c:
    print(1)
    print(a, b, c)
else:
    print(-1)
