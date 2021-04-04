n = int(input())
player=[]
for i in range(n):
    height, weight=map(int, input().split())
    player.append((height, weight))
#키 기준 sort
player.sort(key=lambda x:(x[0], x[1]))
count=0
#마지막 player는 항상 통과, weight비교하기
# 자기보다 키 큰 애들보다 weight가 작으면 False, 아니면 True
for i in range(n):
    flag=True
    for j in range(i+1, n):
        if j!=i and player[i][1]<player[j][1]:
            flag = False
            break
    else:
        count+=1
print(count)