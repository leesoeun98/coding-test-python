import sys
num=[]
for _ in range(int(input())):
    num.append(int(sys.stdin.readline()))
num.sort()
for n in num:
    print(n)