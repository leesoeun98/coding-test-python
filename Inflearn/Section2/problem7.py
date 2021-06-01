import math
n = int(input())
count=0
def isPrime(x):
    if x==1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    else:
        return True
for i in range(1, n+1):
    if isPrime(i):
        count+=1
print(count)


"""
#에라토스테네스 체 이용하기 (배수면 모두 False 처리)
n = int(input())
prime=[True]*(n+1)
prime[1]=False
for i in range(2, n+1):
    if prime[i]:
        for j in range(i+i, n+1, i):
            prime[j]=False
count=0
for i in range(1, n+1):
    if prime[i]:
        count+=1
print(count)
"""