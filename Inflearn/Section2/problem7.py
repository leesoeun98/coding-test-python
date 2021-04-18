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