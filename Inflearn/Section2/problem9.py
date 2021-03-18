def competition(a, b, c):
    if a==b==c:
        return 10000+a*1000
    elif a==b and a!=c:
        return 1000+a*100
    elif a==c and a!=b:
        return 1000+a*100
    elif b==c and a!=c:
        return 1000+b*100
    else:
        return 100*max(a ,b, c)

n=int(input())
answer = []
for i in range(n):
    dice=list(map(int, input().split()))
    answer.append(competition(dice[0], dice[1], dice[2]))
print(max(answer))