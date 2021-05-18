import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    answer = [0] * 4
    if not line:
        break
    else:
        for l in line:
            if l.isdigit():
                answer[2] += 1
            elif l.islower():
                answer[0] += 1
            elif l.isspace():
                answer[3] += 1
            else:
                answer[1] += 1
    print(*answer)
