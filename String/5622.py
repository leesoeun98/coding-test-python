alp=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s=input()
time=0
#입력한 모든 알파벳에 대
for j in range(len(s)):
    # alp의 각 원소에 대해서
    for i in alp:
        #입력알파벳이 해당 원소에 속하면
        if s[j] in i:
            time+=(3+alp.index(i))
print(time)