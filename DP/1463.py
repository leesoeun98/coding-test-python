n=int(input())
count=0
if n==1:
    count=0
elif n<=3:
    count=1
else:
    while n>1:
        n=n-3
        count+=1
        if n%3==0:
            count=(n//3+count-1)
            n//=3
            break
        elif n%2==0:
            count=(count+n//2-1)
            n //= 2
            break
        else:
            n=n-1
            count+=1
print(count)


