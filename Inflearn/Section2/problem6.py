n = int(input())
nums = list(input().split())
answers=[]
for num in nums:
    answer=0
    for nu in num:
        answer+=int(nu)
    answers.append(answer)
for i in range(n):
    if answers[i]==max(answers):
        print(nums[i])
        break

"""
def digit_sum(x):
    digit=list(map(int, str(x)))
    return sum(digit)
n = int(input())
num=list(map(int, input().split()))
res_sum=0
res=0
for n in num:
    d = digit_sum(n)
    if res_sum < d:
        res_sum=digit_sum(n)
        res=n
print(res)
"""
"""
# 자릿수 합 구하기, 정렬 주의 
n = int(input())
num=list(map(int, input().split()))
answer=[]
def digit_sum(x):
    res = 0
    while x>0:
      res+=(x%10)
      x=x//10
    return res

for idx, n in enumerate(num):
  answer.append((digit_sum(n), idx))

# or 밑에도 가능
max=-2147000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
        
answer.sort(key=lambda x:(-x[0], x[1]))
print(num[answer[0][1]])
"""

"""
n = int(input())
numbers=list(map(int, input().split()))
answer=0
answersum=0
def digitSum(x):
    digitsum=0
    while x>0:
        digitsum+=x%10
        x//=10
    return digitsum
for idx, num in enumerate(numbers):
    if answersum<digitSum(num):
        answer=num
        answersum=digitSum(num)
print(answer)
"""