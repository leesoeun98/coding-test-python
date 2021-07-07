from collections import deque
n, m = map(int, input().split())
sub=list(map(int, input().split()))
queue=deque([i for i in range(1, n+1)])
res=0
for i in range(m):
    q_len = len(queue)
    q_index = queue.index(sub[i])
    if q_index< q_len-q_index:
        while True:
            if queue[0]==sub[i]:
                queue.popleft()
                break
            else:
                queue.append(queue.popleft())
                res+=1
    else:
        while True:
            if queue[0]==sub[i]:
                queue.popleft()
                break
            else:
                queue.appendleft(queue.pop())
                res+=1
print(res)


