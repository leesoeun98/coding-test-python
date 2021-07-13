n = int(input())
def calc(num, cnt):
    if num==n:
        print(cnt)
        return
    else:
        calc((num%10)*10+(num//10+num%10)%10, cnt+1)

calc((n%10)*10+(n//10+n%10)%10, 1)

