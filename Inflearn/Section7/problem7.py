from collections import deque
s, e=map(int, input().split())
check=[0 for i in range(10001)]
count=[0 for i in range(10001)]
queue=deque()
# 시작지점 초기화
queue.append(s)
check[s]=1
count[s]=0

while queue:
    cur=queue.popleft()
    if cur==e:
        break
    for next in (cur-1, cur+1, cur+5):
        if 0<next<=10000:
            #방문 안했으면 방문 하고, queue에 넣기
            if check[next]==0:
                queue.append(next)
                check[next]=1
                count[next]=count[cur]+1
print(count[e])