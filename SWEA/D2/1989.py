for t in range(1, int(input())+1):
    word=input()
    for i in range(len(word)//2):
        if word[i]!=word[len(word)-i-1]:
            print("#"+str(t)+" "+str(0))
            break
    else:
        print("#" + str(t) + " " + str(1))