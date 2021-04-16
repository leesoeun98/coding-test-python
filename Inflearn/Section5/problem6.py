#1차 시도 실패 (답안 봄)

from collections import deque

n, m = map(int, input().split())
patient = list(map(int, input().split()))
idxpatient = []
for idx, p in enumerate(patient):
    idxpatient.append((idx, p))
idxpatient = deque(idxpatient)
idx=0
while idxpatient:
    cur = idxpatient.popleft()
    if any(cur[1]< x[1] for x in idxpatient):
        idxpatient.append(cur)
    else:
        idx+=1
        if cur[0]==m:
            print(idx)
            break
"""
from collections import deque
n, m = map(int, input().split())
hurry=list(map(int, input().split()))
patients=[]
for idx, h in enumerate(hurry):
    patients.append((idx, h))
patients=deque(patients)
index=0
while patients:
    first=patients.popleft()
    for i in range(len(patients)):
        if first[1]<patients[i][1]:
            patients.append(first)
            break
    else:
        index += 1
        if first[0]==m:
            print(index)
            break

"""