n = int(input())
num = list(map(int, input().split()))
cnt = 0
prime = [True] * 1001
prime[1] = False
for i in range(1, 1001):
    if prime[i] == True:
        for j in range(i+i, 1001, i):
            prime[j] = False
for n in num:
    if prime[n] == True:
        cnt += 1
print(cnt)
