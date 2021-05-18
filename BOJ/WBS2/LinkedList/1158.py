from collections import deque
n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
queue=deque(people)
answer=[]
while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    answer.append(str(queue.popleft()))
print('<'+', '.join(answer)+'>')
