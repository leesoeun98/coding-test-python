import sys
import statistics
from collections import Counter
n = int(input())
num = []

def avg(num):
    return float(sum(num) / n)
def median(num):
    return statistics.median(num)
def most(num):
    if n==1:
        return num[0]
    #개수 셀 때 counter 쓰기
    c=Counter(num).most_common(2)
    return (c[1][0] if c[0][1]==c[1][1] else c[0][0])
def scope(num):
    return max(num)-min(num)

for _ in range(n):
    num.append(int(sys.stdin.readline()))

#최빈값 때문에 정렬해서 넣어야함 
num=sorted(num)

print(round(avg(num)))
print(median(num))
print(most(num))
print(scope(num))