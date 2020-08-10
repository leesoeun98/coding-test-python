import sys
num=int(input())
words=[]
for _ in range(num):
    words.append(sys.stdin.readline().strip())

#중복 없애기
words=set(words)
# sorted인자로 길이와 사전 순 넣어주기
words=sorted(words, key=lambda word: (len(word), word.lower()))
for i in words:
    print(i)
