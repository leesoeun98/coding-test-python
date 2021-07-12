prime = [True] * 10001
prime[1] = False
prime_num = []

for i in range(1, 10001):
    if prime[i] == True:
        for j in range(i + i, 10001, i):
            prime[j] = False
for i in range(2, 10001):
    if prime[i] == True:
        prime_num.append(i)

for _ in range(int(input())):
    n = int(input())
    res=[]
    for i in range(len(prime_num)):
        if prime[n - prime_num[i]] == True:
            res.append((prime_num[i], n-prime_num[i], abs(n-prime_num[i]-prime_num[i])))
    res.sort(key=lambda x:x[2])
    print(res[0][0], res[0][1])
