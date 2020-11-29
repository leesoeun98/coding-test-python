def solution(paarticipant, completion):
    answer=''
    dic={}
    #1. dic에 participant를 담는다 (동명이인은 1추가, 이외는 1이 value값)
    #->단, 사람 이름을 key값으로 써야 삭제가 된다
    #2. completion에 있는 이름을 dic에서 삭제한다 (1이면 삭제, 1이 아니면 -1)
    #3. 남은 선수 한 명을 반환한다.
    for p in paarticipant:
        if p in dic:
            dic[p]+=1
        else:
           dic[p]=1
    for c in completion:
        if dic[c]==1:
            del(dic[c])
        else:
            dic[c]-=1
    for key in dic.keys():
        answer=key
    return answer


print(solution(["leo","kiki","eden"],["eden","kiki"]))