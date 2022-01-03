# list comprehension
# 리스트를 빠르고 간결하게 처리 : 파이썬 코드 스타일

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i%2==0]
print(result)

# 중첩 반복

ls1 = ['a', 'b', 'c']
ls2 = ['D', 'E', 'F']

result = []
for i in ls1:
    for j in ls2:
        result.append(i+j)
print(result)

result = [i+j for i in ls1 for j in ls2]
print(result)

# 문자열
words = 'Remember to let her into your heart'.split()
print(words)

result = [[w.upper(), w.lower(), len(w)] for w in words]
print(result)