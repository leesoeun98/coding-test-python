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

def isPrime(x):
    flag = True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            flag = False
            return flag
        else:
            flag = True
    return flag

n = int(input())
num=list(map(int, input().split()))
for i in range(n):
  reversed_num=0
  while num[i]>0:
    digit=num[i]%10
    num[i]=num[i]//10
    reversed_num=reversed_num*10+digit
  if isPrime(reversed_num) and reversed_num!=1:
    print(reversed_num)

"""