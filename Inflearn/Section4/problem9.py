#1차 시도 실패
from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
numbers = deque(numbers)
answer = []
answerNumber=[]
if numbers[0] < numbers[-1]:
    answerNumber.append(numbers.popleft())
    answer.append('L')
else:
    answerNumber.append(numbers.pop())
    answer.append('R')
while numbers:
    if numbers[-1] < numbers[0]:
        if answerNumber[-1] < numbers[-1]:
            answerNumber.append(numbers.pop())
            answer.append('R')
    else:
        if answerNumber[-1] < numbers[0]:
           answerNumber.append(numbers.popleft())
           answer.append('L')
    if numbers[0] < answerNumber[-1] and numbers[-1] < answerNumber[-1]:
        break
print(answerNumber)
print(answer)