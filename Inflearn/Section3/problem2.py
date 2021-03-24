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