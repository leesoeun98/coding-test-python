from collections import deque
n, k = map(int, input().split())
distance=[0]*100001
queue=deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x==k:
        print(distance[x])
        break
    for next in (x-1, x+1, 2*x):
        if 0<=next<=100000 and distance[next]==0:
            distance[next]=distance[x]+1
            queue.append(next)
