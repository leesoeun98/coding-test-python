alp=['c=','c-','dz=','d-','lj','nj','s=','z=']
s=input()
#alp의 각 원소에 대해서
for i in alp:
    if i in s:
        # s에 i가 있다면 *로 대체
        s=s.replace(i, "*")
print(len(s))