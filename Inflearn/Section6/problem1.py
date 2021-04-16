def Binary(x):
    if x==0:
        return
    else:
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