word = input()
alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for a in alphabet:
    if a in word:
        word=word.replace(a, "*")
print(len(word))