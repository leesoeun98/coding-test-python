prime = [True] * 1000001
prime[1] = False
prime_num = []
n = int(input())


def check(num):
    lst = list(map(int, str(num)))
    for i in range(len(lst) // 2):
        if lst[i] != lst[-i - 1]:
            return False
    else:
        return True


for i in range(2, 1000001):
    if prime[i] == True:
        for j in range(i + i, 1000001, i):
            prime[j] = False

for i in range(1000001):
    if prime[i] == True and check(i):
        prime_num.append(i)
res=0
for num in prime_num:
    if num >= n:
        res=num
        break
if res==0:
    res=1003001
print(res)
