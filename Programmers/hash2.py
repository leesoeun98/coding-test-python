"""
def solution(phone_book):
    hash={}
    #1. hash에 전화번호 담기
    #2. 전화번호의 각 숫자 쪼개기
    #3. 각 숫자 문자열이 hash에 있고, 같지 않다면 false (단, 자기자신의 번호는 제외)
    for phone_number in phone_book:
        hash[phone_number]=1
    for phone_number in phone_book:
        temp=""
        for number in phone_number:
            temp+=number
            if temp in hash and phone_number!=temp:
                answer=False
                break
    return answer
"""
def solution(phone_book):
    answer=True
    #1. 순서대로 sorting
    #2. 순서대로 이므로, 특정 전화번호가 다음 전화번호에 속하는지만 확인하면 된다
    phone_book=sorted(phone_book)
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer= False
            break
    return answer


print(solution(["12","123","1235","567","88"]))

