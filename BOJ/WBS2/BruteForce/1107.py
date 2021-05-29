channel = int(input())
m = int(input())
# enable도 set
enable = {str(i) for i in range(10)}
if m != 0:
    enable -= set(map(str, (input().split())))
min_cnt = abs(100 - channel)
for i in range(1000001):
    temp = str(i)
    # 망가진 버튼이면 탐색 안함
    for j in range(len(temp)):
        if temp[j] not in enable:
            break
        # 마지막이면
        elif j == len(temp) - 1:
            min_cnt = min(min_cnt, abs(channel - i) + len(str(i)))
print(min_cnt)
