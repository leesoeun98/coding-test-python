def fact(num):
    #0!==1
    if num==0:
        return 1
    #이전 fact호출
    else:
        return num*fact(num-1)

num=int(input())
print(fact(num))