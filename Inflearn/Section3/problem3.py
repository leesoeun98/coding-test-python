# 1차 시도 실패
num = list(range(21))
for _ in range(10):
    start, end = map(int, input().split())
    # 칸 수 //2 만큼 swap
    for i in range((end - start + 1) // 2):
        num[start + i], num[end - i] = num[end - i], num[start + i]
num.pop(0)
print(*num)
