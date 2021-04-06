# 1. 피연산자면 stack에 push
# 2. 연산자 만나면 pop 2번, 계산 후 다시 push
# 3. stack에 남은 마지막 값이 결과

equation=input()
stack=[]
for e in equation:
    if e.isdigit():
        stack.append(int(e))
    else:
        op2=stack.pop()
        op1=stack.pop()
        if e=='+':
            stack.append(op1+op2)
        elif e=='-':
            stack.append(op1-op2)
        elif e=='*':
            stack.append(op1*op2)
        elif e=='/' and op2!=0:
            stack.append(op1/op2)
print(*stack)
