def cal(answer, brown):
    for carpet in answer:
        if carpet[1] < 2:
            tbrown = carpet[0] * carpet[1]
            if tbrown == brown:
                return carpet[0], carpet[1]
        elif carpet[0] < 2:
            tbrown = carpet[0] * carpet[1]
            if tbrown == brown:
                return carpet[0], carpet[1]
        else:
            tbrown = 2 * carpet[0] + 2 * (carpet[1] - 2)
            if tbrown == brown:
                return [carpet[0], carpet[1]]


def solution(brown, yellow):
    answer = []
    size = brown + yellow
    for i in range(1, size+1):
        for j in range(1, size + 1):
            if i * j == size and i >= j:
                answer.append([i, j])
                break
    return cal(answer, brown)