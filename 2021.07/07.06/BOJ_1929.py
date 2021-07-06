m, n = map(int, input().split())
prime=[True]*(n+1)
prime[1]=False

for i in range(2, n+1):
    if prime[i]==True:
        for j in range(i+i, n+1, i):
            prime[j]=False

for i in range(m, n+1):
    if prime[i]==True:
        print(i)