prime=[True]*10001
prime[1]=False
for i in range(2, 10001):
    if prime[i]==True:
        for j in range(i+i, 10001, i):
            prime[j]=False

for _ in range(int(input())):
    n=int(input())
    a = n//2
    b = a
    for _ in range(10000):
        if prime[a] and prime[b]:
            print(a, b)
            break
        a-=1
        b+=1
