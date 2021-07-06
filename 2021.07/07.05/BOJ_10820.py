import sys
while True:
    line = sys.stdin.readline().rstrip('\n')
    answer=[0]*4
    if not line:
        break
    else:
        for l in line:
            if l.islower():
                answer[0]+=1
            elif l.isupper():
                answer[1]+=1
            elif l.isdigit():
                answer[2]+=1
            else:
                answer[3]+=1
    print(*answer)
