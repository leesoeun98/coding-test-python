base1, base2=map(int, input().split())
n = int(input())
num=list(map(int,input().split()))
res=0
#10진수로 먼저 바꾸기
for i in range(n):
    res+=num[len(num)-i-1]*pow(base1, i)
answer=[]
#base2 진법으로 바꾸기
while res:
    answer.append(res%base2)
    res//=base2
print(*answer[::-1])