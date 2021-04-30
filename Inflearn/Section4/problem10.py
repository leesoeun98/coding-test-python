# 1차 시도 실패
# 2차 시도 실패 (답안 봐도 못품)
n = int(input())
reversednum = list(map(int, input().split()))
originalnum = [0 for i in range(n)]

for i in range(n):
    for j in range(n):
        if reversednum[i] == 0 and originalnum[j] == 0:
            originalnum[j] = i + 1
            break
        elif originalnum[j] == 0:
            reversednum[i] -= 1
print(*originalnum)
