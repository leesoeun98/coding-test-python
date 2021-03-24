# 1차 시도 실패
num = [i for i in range(1, 21)]
for _ in range(10):
    start, end = map(int, input().split() - 1)
    for i in range(start, start + end // 2):

num[start:end + 1:-1]
print(num)
