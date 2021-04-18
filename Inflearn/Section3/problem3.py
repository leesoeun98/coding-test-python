card=[i for i in range(1, 21)]
for _ in range(10):
    start, end=map(int, input().split())
    start-=1
    end-=1
    for i in range((end-start+1)//2):
        card[start+i], card[end-i]=card[end-i], card[start+i]
print(*card)
