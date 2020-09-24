def solution(answers):
    math = [0,0,0]
    answer=[]
    math1=[1,2,3,4,5]*2000
    math2=[2,1,2,3,2,4,2,5]*1250
    math3=[3,3,1,1,2,2,4,4,5,5]*1000
    #답안이 10000개이므로

    for i in range(len(answers)):
        if math1[i]==answers[i]:
            math[0]+=1
        if math2[i]==answers[i]:
            math[1]+=1
        if math3[i]==answers[i]:
            math[2]+=1

    for i, j in enumerate(math):
        #최댓값이 여러개일땐 enumerate 사용해서 인덱스를 찾자
        if j==max(math):
            answer.append(i+1)
    return answer

"""
이것도 가능 -> idx이용
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
"""