l = int(input())
boxes=list(map(int, input().split()))
m = int(input())
for _ in range(m):
    maxheight=max(boxes)
    minheight=min(boxes)
    idx=0
    maxIndex=0
    minIndex=0
    #idx 찾기
    while idx<l:
        if boxes[idx]==maxheight:
            maxIndex=idx
        if boxes[idx]==minheight:
            minIndex=idx
        idx+=1
    #높이 조정
    boxes[maxIndex]-=1
    boxes[minIndex]+=1
print(max(boxes)-min(boxes))

"""
l = int(input())
boxes=list(map(int, input().split()))
m = int(input())
for _ in range(m):
    boxes.sort()
    boxes[-1]-=1
    boxes[0]+=1
print(max(boxes)-min(boxes))
"""