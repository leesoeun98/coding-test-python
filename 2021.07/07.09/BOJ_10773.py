n = int(input())
stack=[]
for _ in range(n):
    num=int(input())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
res=0
for s in stack:
    res+=s
print(res)
