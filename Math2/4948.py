import math
import sys
def prime(num):
    # 1이면 소수아님
    if num == 1:
        return False
    # 각 숫자에 대해서 2부터 루트까지 수로 나눠지지 않으면 소수
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

while True:
    n=int(input())
    count=0
    if n==0:
        break
        #이 부분때문에 시간초과되는데, 미리 구해놓고 비교하면 아마 시간 효율적일 듯
        #일단 pypy3으로 통과
    for i in range(n+1, 2*n+1):
        if prime(i):
            count+=1
    print(count)

