import math
def prime(num):
    # 1이면 소수아님
    if num == 1:
        return False
    # 각 숫자에 대해서 2부터 루트까지 수로 나눠지지 않으면 소수
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

m=int(input())
n=int(input())
num=[]

#입력받은 수 모두 검색
for i in range(m,n+1):
    if prime(i):
        num.append(i)
if len(num)==0:
    print(-1)
else:
    print(sum(num))
    print(num[0])