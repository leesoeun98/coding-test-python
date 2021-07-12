n, m = map(int, input().split())
line=[]
each=987654321
whole=987654321
for i in range(m):
    line.append(list(map(int, input().split())))
    each=min(each, line[i][1])
    whole=min(whole, line[i][0])
res=987654321
if n<6:
    res=min(whole, each*n)
else:
    res=[(n//6)*whole+(n%6)*each, ((n//6)+1)*whole, each*n]
    if (n%6)*each>whole:
        res=min(res[0:2])
    else:
        res=min(res)

print(res)
