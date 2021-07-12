n, k = map(int, input().split())
num=list(input())
stack=[]

for nu in num:
    while stack and int(stack[-1])<int(nu) and k>0:
        k-=1
        stack.pop()
    stack.append(nu)

if k>0:
   stack=stack[:-k]
print(''.join(stack))