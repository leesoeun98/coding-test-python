from collections import deque
n,m = map(int, input().split())
hurry=list(map(int, input().split()))
patient=[]
for idx, h in enumerate(hurry):
    patient.append((idx, h))
patient=deque(patient)
cnt=0
while patient:
    cur = patient.popleft()
    for p in patient:
        if cur[1]<p[1]:
            patient.append(cur)
            break
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break


