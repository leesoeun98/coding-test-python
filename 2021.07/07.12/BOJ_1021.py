from collections import deque
n, m = map(int, input().split())
queue=deque([i for i in range(1, n+1)])
num=list(map(int, input().split()))
cnt=0
for n in num:
    if queue.index(n)<len(queue)-queue.index(n):
        while True:
            if queue[0]==n:
                queue.popleft()
                break
            else:
                queue.append(queue.popleft())
                cnt+=1
    else:
        while True:
            if queue[0]==n:
                queue.popleft()
                break
            else:
                queue.appendleft(queue.pop())
                cnt+=1
print(cnt)