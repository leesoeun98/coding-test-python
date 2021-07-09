n, m = map(int, input().split())
lines=[]
res=987654321
whole=100000
each=100000
for _ in range(m):
    lines=list(map(int, input().split()))
    whole=min(whole, lines[0])
    each=min(each, lines[1])

if n>6:
    res=[(n//6+1)*whole, (n//6)*whole+(n%6)*each, each*n]
    if (n%6)*each > whole:
        res=min(res[0:2])
    else:
        res=min(res)
else:
    res=min(whole, each*n)
print(res)
