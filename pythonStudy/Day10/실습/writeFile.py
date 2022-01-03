
# data = 'Hi'
# f = open('file2.txt', 'w')
# f.write(data)
# f.close()


data = '안녕하세요!'
f = open('file3.txt', 'w', encoding='utf-8')

for i in range(1,11):
    data = '%d행\n' %i
    f.write(data)

f.close()