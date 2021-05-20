from collections import deque

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

for _ in range(int(input())):
    num=list(map(int, input().split()))
    num=deque(num)
    num.popleft()
    answer=[]
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            answer.append(gcd(num[i], num[j]))
    print(sum(answer))

