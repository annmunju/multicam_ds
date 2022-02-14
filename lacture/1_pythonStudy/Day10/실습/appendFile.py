
f = open('file3.txt', 'a')

appendData = '\n\nPython Programming'
f.write(appendData)

f = open('file3.txt', 'r')
print(f.read())
f.close()