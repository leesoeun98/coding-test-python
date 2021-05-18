from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
answer = []
# while 사용시 시간 초과 => deque의 rotate 사용하기
while queue:
    #왼쪽으로 가야함 (음수)
    queue.rotate(-k+1)
    answer.append(str(queue.popleft()))
print('<' + ', '.join(answer) + '>')
"""
segment tree 사용해야 함 
"""