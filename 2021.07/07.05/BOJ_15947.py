n = int(input())
lyrics = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby',
          'sukhwan']
res = lyrics[n % 14 - 1]
if res == 'tururu':
    if n // 14 >= 3:
        res = "tu+ru*" + str(n // 14 + 2)
    else:
        res += 'ru' * (n // 14)
elif res == 'turu':
    if n // 14 >= 4:
        res = "tu+ru*" + str(n // 14 + 1)
    else:
        res += 'ru' * (n // 14)

print(res)
