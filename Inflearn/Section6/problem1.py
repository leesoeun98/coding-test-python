def Binary(x):
    if x==0:
        return
    else:
        #재귀함수 호출이 먼저 되어야 맨 마지막거가 출력됨. 즉 뒤부터 출력됨
        Binary(x//2)
        print(x%2, end="")
Binary(int(input()))

"""
num = int(input())
res=[]
def Binary(x):
    if x==0:
        return
    else:
        res.append(str(x%2))
        Binary(x//2)
Binary(num)
res=res[::-1]
answer=''.join(res)
print(answer)
"""