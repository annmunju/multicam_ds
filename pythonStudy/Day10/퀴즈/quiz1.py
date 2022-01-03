yday = open('yesterday.txt', 'r')
lyrics = yday.readlines()
words = []
for line in lyrics:
    word = line.rsplit()
    word = [i.lower() for i in word]
    words += word

wordSet = sorted(set(words))

for w in wordSet :
    print(f'\'{w}\': {words.count(w)}')
