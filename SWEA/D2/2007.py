for i in range(int(input())):
    word = list(input())
    res = 0
    for j in range(1, len(word)):
        if word[:j+1] == word[j+1:2 * j + 2]:
            res = j+1
            break
    print("#" + str(i + 1) + " " + str(res))
