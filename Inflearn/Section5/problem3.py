# 중위 -> 후기
# 1. 피연산자는 바로 출력
# 2. 연산자는 stack의 top보다 우선순위 높거나 같은 것은 pop
# 2. stack의 top보다 우선순위 작은 연산자는 push
# 3. ( 는 무조건 스택에 넣음
# 4. ) 는 (를 만날때까지 스태에서 pop

#1차 시도 답안봄
equation = input()
stack = []
answer = ""
for e in equation:
    if e.isdigit():
        answer += e
    else:
        if e == '(':
            stack.append(e)
        elif e == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()  # ) 제거
        elif e == '+' or e == '-':
            # 가장 낮은 순위 만날때까지 pop
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(e)
        elif e == '*' or e == '/':
            stack.append(e)
while stack:
    answer+=stack.pop()
print(answer)
