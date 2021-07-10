n, m = input().split()
m=int(m)
stack=[]
for nu in n:
    while m>0 and stack and int(stack[-1])<int(nu):
        stack.pop()
        m-=1
    stack.append(str(nu))
if m>0:
    stack=stack[:-m]
print(''.join(stack))