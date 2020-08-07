num=int(input())
count=0
for _ in range(num):
    s=input()
    for i in range(len(s)):
        #마지막 문자 제외
        if i!=len(s)-1:
            # 문자열 같은 동안은 pass
            if s[i]==s[i+1]:
                pass
            # 문자열 다른데 앞에 있는 문자열이 뒤에 속해있다면 break
            elif s[i] in s[i+1:]:
                break
        else:
            count+=1

print(count)

