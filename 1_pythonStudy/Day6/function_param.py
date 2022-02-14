'''
# 함수의 매개변수

# 매개변수(parameter) : 함수 정의시 함수로 전달되는 값을 받는 변수
def getArea(매개변수1, 매개변수2):
    return 매개변수1*매개변수2

# 인수(argument) : 함수 호출 시 함수에게 전달되는 값.
인수1 = 10
인수2 = 5
# print(getArea(인수1, 인수2))

def getAvg(k, e, m):
    return (k+e+m)/3

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
math = int(input('수학점수 입력 : '))

print('평균:', getAvg(kor, eng, math))
'''

def showNames(names):
    for name in names:
        print(name)

nameList = ['홍길동', '강감찬', '이순신']
showNames(nameList)

# 가변길이 매개변수 : *args(인수), **kwargs(키,값)
def func(*hi):
    total = 0
    for x in hi:
        total += x
    return total

print(func(1,2,3,4,5))

def showNames(*names):
    for name in names:
        print(name,end=' ')
    print()

showNames('홍길동', '강감찬')
showNames('홍길동', '강감찬', '유관순', '이순신')

# **kwargs 예제

def showInfo(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print()
    for value in kwargs.values():
        print(value, end=' ')
    print()
    for item in kwargs.items():
        print(item,end=' ')
    print()
    
showInfo(name='홍길동', id='123', phone='010-111-1111')