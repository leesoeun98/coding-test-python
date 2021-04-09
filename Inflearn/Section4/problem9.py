#1차 시도 실패
#2차 시도 실패 (답안도 이해 못함)

from collections import deque
n = int(input())
num=list(map(int, input().split()))
answer=""
num=deque(num)
arr=[]
while num:
    if len(arr)==0:
        if num[0]<num[-1]:
            arr.append(('L', num.popleft()))
        else:
            arr.append(('R', num.pop()))
    else:
        if num[0]<num[-1]:
            if arr[-1][1]<num[0]:
                arr.append(('L', num.popleft()))
            elif arr[-1][1]<num[-1]:
                arr.append(('R', num.pop()))
            elif arr[-1][1]>=num[0] and arr[-1][1]>=num[-1]:
                break

        else:
            if arr[-1][1]<num[-1]:
                arr.append(('R', num.pop()))
            elif arr[-1][1]<num[0]:
                arr.append(('L', num.popleft()))
                break
            elif arr[-1][1]>=num[0] and arr[-1][1]>=num[-1]:
                break
for letter, number in arr:
    answer+=letter
print(answer)
print(len(answer))