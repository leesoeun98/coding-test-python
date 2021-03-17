n, k = map(int, input().split())
num = list(map(int, input().split()))
answer = []
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            answer.append(num[i] + num[l] + num[j])
answer = list(set(answer))
answer = sorted(answer, reverse=True)
print(answer[k-1])
