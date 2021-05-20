n = int(input())
num=list(map(int, input().split()))
def isPrime(n):
    if n==1:
        return False
    else:
        for i in range(2, n//2+1):
            if n%i==0:
                return False
        else:
            return True
count=0
for n in num:
    if isPrime(n):
        count+=1
print(count)