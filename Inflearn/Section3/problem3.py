# 1차 시도 실패
num = list(range(21))
for _ in range(10):
    start, end = map(int, input().split())
    # 칸 수 //2 만큼 swap
    for i in range((end - start + 1) // 2):
        num[start + i], num[end - i] = num[end - i], num[start + i]
num.pop(0)
print(*num)
"""
number = [i for i in range(1, 21)]
for _ in range(10):
    a, b = map(int, input().split())
    a-=1
    b-=1
    for i in range((b - a + 1) // 2):
        number[a + i], number[b - i] = number[b - i], number[a + i]
print(*number)
"""