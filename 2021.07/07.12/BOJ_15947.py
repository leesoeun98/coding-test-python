lyrics = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby',
          'sukhwan']
n = int(input())
word = lyrics[(n % len(lyrics))-1]

if word=='tururu':
    if n//len(lyrics)>2:
        print("tu+"+"ru*"+str(2+n//len(lyrics)))
    else:
        print("tu"+"ru"*(2+n//len(lyrics)))
elif word=='turu':
    if n//len(lyrics)>3:
        print("tu+"+"ru*"+str(1+n//len(lyrics)))
    else:
        print("tu"+"ru"*(1+n//len(lyrics)))
else:
    print(word)