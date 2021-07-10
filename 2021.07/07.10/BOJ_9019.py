from collections import deque
import sys
def bfs(start):
    queue=deque()
    queue.append([start, ""])
    distance[start]=1
    while queue:
        x, d = queue.popleft()
        if x==end:
            return d
        if 2*x<=9999 and distance[2*x]==0:
            distance[2*x]=1
            queue.append([2*x, d+"D"])
        if 2*x>9999 and distance[(2*x)%10000]==0:
            distance[(2 * x) % 10000] =1
            queue.append([(2*x)%10000, d+'D'])
        if x-1>=0 and distance[x-1]==0:
            distance[x-1]=1
            queue.append([x-1, d+'S'])
        if x-1<0 and distance[9999]==0:
            distance[9999]=1
            queue.append([9999,d+'S'])
        nx = int((x%1000)*10 + x/1000)
        if distance[nx]==0:
            distance[nx]=1
            queue.append([nx, d+'L'])
        nx=int((x%10)*1000+x/10)
        if distance[nx]==0:
            distance[nx]=1
            queue.append([nx, d+'R'])

for _ in range(int(input())):
    start, end = map(int, sys.stdin.readline().split())
    distance=[0]*10001
    print(bfs(start))
