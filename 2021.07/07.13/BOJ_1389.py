n, m = map(int, input().split())
tree=[[n]* (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    tree[a][b]=1
    tree[b][a]=1
#플로이드 와샬 문제
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1 ,n+1):
            if i==j:
                tree[i][j]=0
            else:
                tree[i][j]=min(tree[i][j], tree[i][k]+tree[k][j])

res=[]
for each in tree:
    res.append(sum(each))
print(res.index(min(res)))
