# 수의 범위가 작으면 counting sort
import sys
n=int(input())
num=[0 for i in range(10001)]
for i in range(n):
    num[int(sys.stdin.readline())]+=1
for i in range(10001):
    if num[i]!=0:
        for j in range(num[i]):
            print(i)