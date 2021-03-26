n = int(input())
boxes=list(map(int, input().split()))
m = int(input())

maxHeight=max(boxes)
minHeight=min(boxes)
minIndex=0
maxIndex=0
for i in range(m):
    for j in range(n):
        if boxes[j]==maxHeight:
            maxIndex=j
            for k in range(n):
                if boxes[k]==minHeight:
                    minIndex=k
    boxes[maxIndex]-=1
    boxes[minIndex]+=1
    minHeight=min(boxes)
    maxHeight=max(boxes)
print(max(boxes)-min(boxes))