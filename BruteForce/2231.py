n=int(input())

def eachnum(num):
    #각 자릿수를 모두 더하는 함수
    sum=0
    while num>0:
        sum+=num%10
        num=num//10
    return sum


def cal(n):
    for i in range(n):
        if i+eachnum(i)==n:
            #자기자신과 자릿수를 더한게 n이 된다면 해당하는 i는 n의 생성자이다.
            return i
    return 0

if cal(n)==0:
   print(0)
else:
    print(cal(n))

"""
n=int(input())
result=0
for i in range(n+1):
    num=list(map(int, str(i)))
    if i+sum(num)==n:
        print(i)
        break
    if i==n:
        print(0)
        """