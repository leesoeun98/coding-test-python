n=int(input())

for _ in range(n):
    m=int(input())
    cache=[0 for _ in range(m+1)]
    #insert써야 오류가 안남...
    cache.insert(1,1)
    countzero = 0
    countone = 0
    for i in range(2, m + 1):
        cache[i] = cache[i - 2] + cache[i - 1]
        if i == 0 or i - 1 == 0 or i - 2 == 0:
            countzero += 1
        if i == 1 or i - 1 == 1 or i - 2 == 1:
            countone += 1
    print(countzero, countone)






