# 1차에 자료 참고하고 풂
import heapq
minheap=[]
while True:
    n = int(input())
    if n==-1:
        break
    else:
        if n==0:
            if len(minheap)==0:
                print(-1)
            else:
                print(heapq.heappop(minheap))
        else:
            heapq.heappush(minheap, n)