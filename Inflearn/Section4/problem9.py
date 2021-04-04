#1차 시도 실패
#2차 시도 실패 (답안도 이해 못함)

n = int(input())
num=list(map(int, input().split()))
answer=""
arr=[]
left=0
right=n-1
last=0
while left<=right:
    if num[left]>last:
        arr.append((num[left], 'L'))
    if num[right]>last:
        arr.append((num[right], 'R'))
    arr.sort()
    if len(arr)==0:
        break
    else:
        answer+=arr[0][1]
        last=arr[0][0]
        if arr[0][1]=='L':
            left+=1
        else:
            right-=1
    arr.clear()
print(len(answer))
print(answer)

