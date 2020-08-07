num=int(input())

def hanoi(n,start, mid, end):
    if n==1:
        print(start, end)
    else:
        #n-1개를 start -> mid
        hanoi(n-1, start, end, mid)
        #1개를 start-> end하고 print
        print(start, end)
        #mid가 start 취급, n-1개 mid -> start
        hanoi(n-1, mid, start, end)

print(2**num-1)
hanoi(num,1,2,3)