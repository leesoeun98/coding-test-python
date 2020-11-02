import sys
n=int(sys.stdin.readline())
dots=[]
for _ in range(n):
    # 좌표 입력 받기
    x, y=map(int, sys.stdin.readline().split())
    # 좌표 배열 형태로 배열에 넣기
    dots.append([x, y])
# 배열 오름차순 정렬 
dots=sorted(dots)

for x, y in dots:
    print(x, y)