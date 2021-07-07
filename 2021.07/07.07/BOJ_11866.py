from collections import deque

n, k = map(int, input().split())
people=[i for i in range(1, n+1)]
people=deque(people)
res=[]
while people:
    for i in range(k-1):
        people.append(people.popleft())
    res.append(str(people.popleft()))
print("<"+', '.join(res)+">")
