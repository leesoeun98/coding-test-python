#1차 시도 실패
#2차 시도 실패 (답안 봐도 못품)
n = int(input())
reversed=list(map(int, input().split()))
answer=[0 for i in range(n)]
for i in range(n):
    for j in range(n):
        #자리 배치 후 break로 멈춤
        if reversed[i]==0 and answer[j]==0:
            answer[j]=i+1
            break
        elif answer[j]==0:
            reversed[i]-=1
print(*answer)