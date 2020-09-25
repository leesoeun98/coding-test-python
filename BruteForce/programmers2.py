from itertools import permutations
import math
def prime(num):
    if num<2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        #permutation 결과를 join으로 합치고 list로 변환하기
        perlist=set(list(map(''.join, permutations(list(numbers),i))))
        for j in list(perlist):
            if prime(int(j)):
                answer.append(int(j))
    #0이 앞에 나올경우 중복되므로 set으로 중복제거 
    answer=list(set(answer))

    return len(answer)