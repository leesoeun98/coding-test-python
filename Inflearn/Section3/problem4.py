"""
n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
number = sorted(first + second)
print(number)
"""
n = int(input())
first = list(map(int, input().split()))
m = int(input())
second = list(map(int, input().split()))
idx1 = idx2 = 0
answer = []
while idx1 < n and idx2 < m:
    if first[idx1] <= second[idx2]:
        answer.append(first[idx1])
        idx1 += 1
    else:
        answer.append(second[idx2])
        idx2 += 1
if idx1 < n:
    answer = answer + first[idx1:]
if idx2 < m:
    answer = answer + second[idx2:]
print(*answer)
