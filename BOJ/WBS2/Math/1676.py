res=1
n = int(input())
for i in range(n, 0, -1):
    res=res*i
ans = list(reversed(list(str(res))))

count=0
for a in ans:
    if int(a)!=0:
        break
    else:
        count+=1
print(count)