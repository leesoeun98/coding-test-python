n, m = map(int, input().split())


# 0의 개수는 숫자가 갖고 있는 2의 개수, 5의 개수 중 최소 (예로 2가 3개 5가 2개면 2개)
# countNum의 경우 n! 안에 num이 몇 번 있는지 세는 함수 (예로 10!면 2가 5번 존재)
def countNum(n, num):
    count = 0
    while n != 0:
        n = n // num
        count += n
    return count


# n! / m!(n-m)! 구현
print(min(countNum(n, 2) - countNum(m, 2) - countNum(n - m, 2), countNum(n, 5) - countNum(m, 5) - countNum(n - m, 5)))
"""numerator = 1
m = min(n - m, m)
for i in range(n, n - m, -1):
    numerator *= i
denominator = 1

for i in range(1, m + 1):
    denominator *= i
res=numerator / denominator
ans=list(reversed(list(str(int(res)))))

count=0
for a in ans:
    if int(a)!=0:
        break
    else:
        count+=1
print(count)
시간 초과 """
