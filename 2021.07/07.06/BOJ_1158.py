from collections import deque
n, k = map(int, input().split())
people=[i for i in range(1, n+1)]
queue=deque(people)
res=[]

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    res.append(str(queue.popleft()))

print("<"+', '.join(res)+">")
