import math
import sys
#매번 소수인지 판별하면 시간 초과 남 미리 소수인 숫자의 boolean 배열 만들어서 해당
#index 값이 true인지 보는게 빠름
# 소수 구하는건 에라토스테네스의 체를 이용하기
def prime(n):
    nums=[True]*(n+1)
    for i in range(2, int(math.sqrt(n)+1)):
        #i가 소수라면 i 배수 모두 false로 바꾸기
        if nums[i]==True:
            for j in range(i+i, n, i):
                nums[j]=False
    return [[i for i in range(2, n) if nums[i]==True], nums]

primes=prime(1000000)[0]
primes_bool = prime(1000000)[1]

while True:
    num=int(sys.stdin.readline())
    if num==0:
        break
    else:
        for i in range(len(primes)):
            if primes_bool[num-primes[i]]==True:
                print("%d = %d + %d" %(num,primes[i],num-primes[i]))
                break
        else:
            print("Goldbach's conjecture is wrong.")