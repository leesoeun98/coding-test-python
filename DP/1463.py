n=int(input())
#1에서 +1하거나 *3하거나 *2하는 방식으로 구하자.
result=[0]*(n+1)
if n==1:
    result[1]=0
else:
    for i in range(2, n+1):
        result[i]=result[i-1]+1
        if i%3==0 and result[i]>result[i//3]+1:
            result[i]=result[i//3]+1
        elif i%2==0 and result[i]>result[i//2]+1:
            result[i]=result[i//2]+1
print(result[n])