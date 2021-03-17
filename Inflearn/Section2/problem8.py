import math
def reverse(x):
    newnum = int(str(x)[::-1])
    isPrime(newnum)

def isPrime(x):
    flag = False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            flag = False
            break
        else:
            flag = True
    if flag==True or x==2:
        print(x)

_ = int(input())
nums = list(map(int, input().split()))
for num in nums:
    reverse(num)
