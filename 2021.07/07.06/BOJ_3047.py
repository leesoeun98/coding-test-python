num = list(map(int, input().split()))
order = input()
num.sort()
for o in order:
    if o=='A':
        print(num[0], end=" ")
    elif o=='B':
        print(num[1], end=" ")
    else:
        print(num[2], end=" ")