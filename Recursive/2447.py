num=int(input())

def triangle(i, j, num):
    if (i//num)%3==1 and (j//num)%3==1:
        print(" ", end="")
    else:
        if num//3==0:
            print("*", end="")
        else:
            triangle(i, j, num//3)

for i in range(num):
    for j in range(num):
        #예로 num이 27이면 삼각형 27번 그리는
        triangle(i, j, num)
    print()