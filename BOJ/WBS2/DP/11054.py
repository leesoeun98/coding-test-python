n = int(input())
num = list(map(int, input().split()))
inc = [1] * n
dec = [1] * n
dp=[0]*n
# 증가
for i in range(n):
    for j in range(i):
        if num[i] > num[j] and inc[i] < inc[j] + 1:
            inc[i] = inc[j]+1
# 감소
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if num[i] > num[j] and dec[i] < dec[j] + 1:
            dec[i] = dec[j]+1
    #inc는 i시점까지 증가, dec는 i부터 n까지 감소
    dp[i]=dec[i]+inc[i]-1
print(max(dp))
