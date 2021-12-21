# 입력 함수 : input(). 키보드로부터 값을 입력 받아서 처리하기 위해
# 입력 함수를 사용해서 입력하면 문자열로 저장됨.

x = 100
y = 300

print(x+y)

name = input('이름: ')
age = int(input('나이: '))

print('이름은 %s이고, 나이는 %d세 입니다.' % (name, age))