n = int(input())
reversedNum = list(map(int, input().split()))
original = [0 for _ in range(n)]
for i in range(n):
    for j in range(n):
        if original[j] == 0 and reversedNum[i] == 0:
            original[j] = i + 1
            break
        # 빈칸일때만 빼야함
        elif original[j]==0 and reversedNum[i]!=0:
            reversedNum[i] -= 1
print(original)
