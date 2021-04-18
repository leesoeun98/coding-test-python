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

"""
# 숫자 뒤집기는 앞으로 이렇게
import math
n = int(input())
num = list(map(int, input().split()))


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    else:
        return True


def reverse(x):
    res = 0
    while x > 0:
        digit = x % 10
        x //= 10
        res = res*10+ digit
    return res

for n in num:
    if isPrime(reverse(n)):
        print(reverse(n), end=" ")
"""