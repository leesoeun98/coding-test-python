import sys

n=int(input())
dots=[]
for _ in range(n):
    x, y=map(int, sys.stdin.readline().strip().split())
    dots.append([x, y])
#정렬 라이브러리 사용 -> sorted는 안정 정렬 
dots=sorted(dots)
for i in range(len(dots)):
    print(dots[i][0], dots[i][1])