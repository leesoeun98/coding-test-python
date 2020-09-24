n=int(input())
big=[]
rank=[]
k=1
for _ in range(n):
    big.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        #각 원소에 접근해서 키끼리 빅, 몸무게끼리 비교하고 크다면 k를 1증가 (k는 나보다 큰 사람의 수)
        if big[i][0]<big[j][0] and big[i][1]<big[j][1]:
            k+=1
    rank.append(k)
    k=1
for i in rank:
    print(i, end=" ")