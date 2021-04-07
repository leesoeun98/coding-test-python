word = input()
num =""
number=0
for w in word:
    if w.isdigit():
        #number = number*10+int(w)
        if len(num)==0 and int(w)==0:
            continue
        else:
            num+=w
number = int(num)
count = 0
for i in range(1, number+1):
    if number % i == 0:
        count += 1
print(num)
print(count)
"""
#숫자 만들기는 res=res*10+w로 
word=input()
res=0
count=0
for w in word:
    if w.isdigit():
        res=res*10+int(w)
print(res)
for i in range(1, res+1):
    if res%i==0:
        count+=1
print(count)
"""