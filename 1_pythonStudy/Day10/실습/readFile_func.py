# read() : 내용 전체를 읽어서 1개의 문자열로 반환

f = open('file2.txt', 'r')

data = f.read()

print(data)
print(type(data))
print(len(data))

f.close()

for ch in data:
    print(ch, end='\t')