n, m, k = map(int, input().split())
res=[]
def team(n, m):
    return min(n//2, m)

for i in range(k+1):
    res.append(team(n-i, m-(k-i)))
print(max(res))

