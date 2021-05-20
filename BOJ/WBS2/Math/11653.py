n = int(input())
answer = []
#break를 해줘야 항상 작은 수로 나뉘어짐.
while n != 1:
    for i in range(2, n+1):
        if n % i == 0:
            print(i)
            n //= i
            break
