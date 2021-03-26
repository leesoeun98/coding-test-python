n = int(input())
player = []
for _ in range(n):
    player.append(list(map(int, input().split())))
player.sort()
# 마지막 지원자는 항상 통과 (키가 제일 커서)
count = 1
for i in range(n - 1):
    flag = True
    for j in range(i + 1, n):
        if player[i][1] > player[j][1]:
            flag = True
        else:
            flag = False
            break
    if (flag):
        count += 1
print(count)
