n, m = map(int, input().split())
adj=[[0 for i in range(n)] for i in range(n)]
for i in range(m):
    start, end, weight=map(int, input().split())
    adj[start-1][end-1]=weight
for arr in adj:
    print(*arr)