n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
for idx, bi in enumerate(b):
    res.append((idx, bi))
res.sort(key=lambda x: x[1])
a.sort(reverse=True)
s=0
for i in range(n):
    s+=res[i][1]*a[i]
print(s)