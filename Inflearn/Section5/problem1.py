num, rm = map(int, input().split())
stack=[]
number=list(str(num))
#큰 수만 stack에 넣고 작으면 pop
for n in number:
    while stack and rm>0 and int(stack[-1])<int(n):
        stack.pop()
        rm-=1
    stack.append(n)
if rm!=0:
    stack=stack[:-rm]
print(''.join(stack))