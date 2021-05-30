import sys

n, m = map(int, input().split())
rect = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
res = 0
# |||
for i in range(1, m - 1):
    for j in range(i + 1, m):
        s1 = sum([rect[x][y] for x in range(n) for y in range(i)])
        s2 = sum([rect[x][y] for x in range(n) for y in range(i, j)])
        s3 = sum([rect[x][y] for x in range(n) for y in range(j, m)])
        res = max(res, s1 * s2 * s3)
# |=
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[x][y] for x in range(n) for y in range(j)])
        s2 = sum([rect[x][y] for x in range(i) for y in range(j, m)])
        s3 = sum([rect[x][y] for x in range(i, n) for y in range(j, m)])
        res = max(res, s1 * s2 * s3)

# =|
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[x][y] for x in range(i) for y in range(j)])
        s2 = sum([rect[x][y] for x in range(i, n) for y in range(j)])
        s3 = sum([rect[x][y] for x in range(n) for y in range(j, m)])
        res = max(res, s1 * s2 * s3)

# --
# ||
for i in range(1, n):
    for j in range(1, m):
        s1 = sum([rect[x][y] for x in range(i) for y in range(m)])
        s2 = sum([rect[x][y] for x in range(i, n) for y in range(j)])
        s3 = sum([rect[x][y] for x in range(i, n) for y in range(j, m)])
        res = max(res, s1 * s2 * s3)

# ||
# --
for i in range(1, m):
    for j in range(1, n):
        s1 = sum([rect[x][y] for x in range(j) for y in range(i)])
        s2 = sum([rect[x][y] for x in range(j) for y in range(i, m)])
        s3 = sum([rect[x][y] for x in range(j, n) for y in range(m)])
        res = max(res, s1 * s2 * s3)

# -
# -
# -

for i in range(1, n-1):
    for j in range(i+1, n):
        s1= sum([rect[x][y] for x in range(i) for y in range(m)])
        s2 = sum([rect[x][y] for x in range(i,j) for y in range(m)])
        s3 = sum([rect[x][y] for x in range(j,n) for y in range(m)])
        res=max(res, s1*s2*s3)
print(res)