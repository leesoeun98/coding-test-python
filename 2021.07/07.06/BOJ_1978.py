n = int(input())
num=list(map(int, input().split()))
prime=[True]*(1001+1)
prime[1]=False
for i in range(2, 1001):
    if prime[i]==True:
        for j in range(i+i, 1001, i):
            prime[j]=False
cnt=0
for n in num:
    if prime[n]==True:
        cnt+=1
print(cnt)