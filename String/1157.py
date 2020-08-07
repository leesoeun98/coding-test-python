s=input()
alp=[0]*26

for i in range(len(s)):
    #입력 시 대소문자 둘다 받으므로 구분해서 센
    if 'A'<=s[i]and s[i]<='Z':
        alp[ord(s[i])-ord('A')]+=1
    else:
        alp[ord(s[i]) - ord('a')] += 1

count=0
maxalp=max(alp)

#최대값 여러개일 때 -> enumerate이용해서 셀 수 있음
for i, j in enumerate(alp):
    if j==maxalp:
        count+=1
        idx=i

if count>1:
    print('?')
else:
    print(chr(idx+65))
