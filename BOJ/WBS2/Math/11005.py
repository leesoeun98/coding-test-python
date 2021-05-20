digit = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num, base = map(int, input().split())
answer = ""

while num:
    answer += str(digit[num % base])
    num //= base
print(answer[::-1])
