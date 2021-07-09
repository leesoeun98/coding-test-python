n, k = map(int, input().split())
num=list(map(int, input()))
stack=[]
for n in num:
    while k>0 and stack and int(stack[-1])<n:
        k-=1
        stack.pop()
    stack.append(str(n))
if k>0:
    stack=stack[:-k]
print(''.join(stack))