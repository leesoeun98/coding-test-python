n, m = map(int, input().split())
num=list(map(int, input().split()))
left=0
right=1
count=0
#값이 커지면 left 늘려서 수열을 줄이고, 값이 작아지면 right늘려서 수열 늘림
while left<=right and right<n:
    sumnum=sum(num[left:right+1])
    if sumnum==m:
        count+=1
        right+=1
    elif sumnum<m:
        right+=1
    elif sumnum>m:
        left+=1
print(count)