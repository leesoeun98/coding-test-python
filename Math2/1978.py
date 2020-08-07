import math
n=int(input())
num=list(map(int, input().split()))
count=n
#입력받은 수 모두 검색
for j in num:
    #1이면 소수아님
    if j==1:
        count-=1
    #각 숫자에 대해서 2부터 루트까지 수로 나눠지지 않으면 소수
    for i in range(2, int(math.sqrt(j))+1):
        if j%i==0:
            count-=1
            break
print(count)