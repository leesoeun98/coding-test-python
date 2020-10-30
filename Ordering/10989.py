import sys
n=int(sys.stdin.readline())

#이렇게 미리 지정안하면 메모리초과 에러 뜸
num=[0]*10001
for _ in range(n):
    #입려된 수를 인덱스로 삼아 언급된 횟수를 저장
    num[int(sys.stdin.readline())]+=1

for i in range(len(num)):
    #언급된 예제만 출력
    if num[i]!=0:
        #개수만큼 반복 출력
        while(num[i]>0):
            print(i)
            num[i]-=1