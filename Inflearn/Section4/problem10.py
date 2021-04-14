#1차 시도 실패
#2차 시도 실패 (답안 봐도 못품)
n = int(input())
reversed=list(map(int, input().split()))
answer=[0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if answer[j]==0 and reversed[i]==0:
            answer[j]=i+1
            break
        elif answer[j]==0:
            reversed[i]-=1
print(*answer)