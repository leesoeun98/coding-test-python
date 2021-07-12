n = int(input())
distance=[[987654321]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i]=0
while True:
    s, e = map(int, input().split())
    if s==-1 and e==-1:
        break
    else:
        distance[s][e]=1
        distance[e][s]=1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j]=min(distance[i][j], distance[i][k]+distance[k][j])

res=[0]*(n+1)
score=100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], distance[i][j])
    score=min(score, res[i])
candidate=[]
for i in range(1, n+1):
    if res[i]==score:
        candidate.append(i)
print(score, len(candidate))
print(*candidate)