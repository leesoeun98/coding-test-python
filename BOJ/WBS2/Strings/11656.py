word = input()
answer=[]
for i in range(len(word)):
    answer.append(word[i:])
answer.sort()
for a in answer:
    print(a)
