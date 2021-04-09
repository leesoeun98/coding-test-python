player = []
for _ in range(int(input())):
    height, weight = map(int, input().split())
    player.append((height, weight))
player.sort(key=lambda x: (x[0], x[1]))
count = 0
# i 번째 선수는 그 다음부터 끝까지 선수들의 무게로만 비교하면 됨
# i번째 선수는 1부터 i-1보다 키가 크니까, i+1부터 끝까지 무게로 더 커야 함
for i in range(len(player)):
    for j in range(i + 1, len(player)):
        if player[i][1] <= player[j][1]:
            break
    else:
        count += 1
print(count)
