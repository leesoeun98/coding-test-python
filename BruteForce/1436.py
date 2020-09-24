n=int(input())

i=666
count=0
while True:
    if '666' in str(i):
        #369게임 참고
        #숫자를 문자열로 취급하면 각 자릿수를 쉽게 쪼갤 수 있음 문자열내에 666이 있는지 확인
        count+=1
    if count==n:
        print(i)
        break
    i+=1