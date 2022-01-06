# 파이썬이 처리하는 자료형 (data type)
# 정수, 실수, 문자열, 불리언(논리형)


a = 100
b = 3.14
c = 'name'
d = True

print(f'{type(a)}\n{type(b)}\n{type(c)}\n{type(d)}')

# 형변환
strA = str(a)
print(f'{type(strA)}')

str1 = str(3.14)
print(str1+'pie')

str2 = '123'
num1 = int(str2)
print(type(num1))

num1 = float(str1)
print(type(num1))
print(num1 + 10)

print(type(str(100)))

print(int('1010',2))
print(int('1010',16))
print(int('1010',8))