n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))
num=sorted(num)

for i in num:
    print(i)

"""
버블정렬
=> 큰 것을 맨 뒤로 뻬면서 제외하는 방식
=> 바로 가까이에 있는 두 숫자끼리 비교해서 당장 더 작은 숫자를 앞으로 보내주는 것을 반복해서 구현

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

for i in range(n):
    #가장 뒤에 있는 원소는 제외
    # i 한번 수행시 가장 큰 값이 뒤로 보내지고 그 수를 제외하고 다시 정렬 반복
    for k in range(n-i-1):
        #앞이 더 크면 앞뒤 바꿔서 큰 수를 뒤로 보냄
        if num[k] >= num[k+1]:
            temp=num[k+1]
            num[k+1]=num[k]
            num[k]=temp
for i in num:
    print(i)
"""

"""
삽입정렬
=> 각 숫자를 적절한 위치에 삽입하여 정렬
=> 다른 정렬과 달리 삽입정렬은 필요할 때만 위치 바꿈 (다른 정렬은 반드시 자리바꿈 수행)

n=int(input())
num=[]
for _ in range(n):
    num.append(int(input()))

for i in range(n):
# 현재 위치 i에서부터 삽입할 위치 선정 시작
# j 앞은 이미 정렬된 것으로 간주
    j=i
    while(j>0):
        # 앞 뒤 숫자 2개 비교해서 적절한 위치에서 값 바꿈
        if(num[j-1]>num[j]):
            temp=num[j]
            num[j]=num[j-1]
            num[j-1]=temp
        j-=1
for i in num:
    print(i)

"""
"""
선택정렬
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

# 마지막 원소는 자동 정렬되므로 배열크기-1 만큼 반복
for i in range(n - 1):
    #최솟값을 각 회전에 해당하는 인덱스로 초기화 
    least = i
    # 그 다음 자료부터 마지막 자료까지 비교해서 최솟값 찾기 
    for j in range(i + 1, n, 1):
        if (num[j] < num[least]):
            least = j
    #최솟값 찾은 후 해당 회전 위치 숫자와 교환 
    #예로 첫번째 회전이면 첫번쨰 자리 숫자와 최솟값 교환 
    if i is not least:
        temp = num[i]
        num[i] = num[least]
        num[least] = temp

for i in num:
    print(i)
"""