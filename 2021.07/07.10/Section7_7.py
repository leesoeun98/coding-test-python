from collections import deque
queue=deque()
s, e = map(int, input().split())
distance=[0]*10001
queue.append(s)

while queue:
    cur = queue.popleft()
    if cur==e:
        break
    for next in (cur-1, cur+1, cur+5):
        if 0<next<=10000 and distance[next]==0:
            distance[next]=distance[cur]+1
            queue.append(next)
print(distance[e])