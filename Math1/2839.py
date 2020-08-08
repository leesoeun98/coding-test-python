n=int(input())
count=0
i=0
if n>=5:
    #5로 나눠질 때
    if n%5==0:
        count=n//5
    #3,5로 구성됐거나 3으로만 구성됐을 때, 안 나눠질 때
    else:
        while n>0:
            #3으로 구성됐으니 3 먼저 빼기
            #3으로 나누는 부분은 여기서 실행
            n-=3
            i+=1
            #5로 나눠질 때 -> 더이상 실행 안해봐도 됨.
            if n%5==0:
                count=i+n//5
                break
            #3으로 나눠질 때 -> 5로 나눠질 수도 있으므로 계속 실행해야하므로 break 안 씀
            elif n%3==0:
                count=i
            #둘다 안 나눠질 때 -> 어차피 n이 0보다 작아지면 끝나므로 break 안 씀
            else:
                count=-1
#5보다 작을 때
else:
    if n%3==0:
        count=n//3
    else:
        count=-1
print(count)