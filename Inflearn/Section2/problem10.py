n = int(input())
answer = list(map(int, input().split()))
score = 0
i = 0
while i < n:
    s = 0
    if answer[i] == 0:
        s = 0
        i += 1
    else:
        while i<n and answer[i] != 0:
            s += 1
            score += s
            i += 1
print(score)
"""
n=int(input())
score=list(map(int, input().split()))
total=0
part=0
for s in score:
    if s==0:
        part=0
    else:
        part+=1
        total+=part
print(total)
"""