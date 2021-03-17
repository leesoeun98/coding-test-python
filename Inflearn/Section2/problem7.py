import math
n = int(input())
count = 0
for j in range(2, n+1):
    flag = True
    for i in range(2, int(math.sqrt(j)) + 1):
        if j % i != 0:
            flag = True
        else:
            flag = False
            break
    if flag == True:
        count+=1
print(count)