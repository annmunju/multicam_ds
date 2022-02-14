# 사각형의 넓이 계산 함수 정의

def getArea():
    width = int(input('가로 : '))
    height = int(input('세로 : '))
    return width * height

print(getArea())

# 3개의 리턴값을 각각 a,b,c로 받기

def multi_return():
    return 1, 2, 3
print(type(multi_return()))

a, b, c = multi_return()
print(a,'\t',b,'\t',c)

def multi_return(): #함수는 위에서 아래로 순서대로 수행
    return 1 # 여기서 리턴값 반환 후 종료
    return 2 # 수행X
    return 3 # 수행X

print(multi_return())

# 리스트 반환
# 3명 이름을 입력 받아 리스트에 저장하고 리스트를 반환하는 함수

def get_names():
    names = []
    for i in range(3):
        name = input('이름 입력: ')
        names.append(name)
    return names

ls = get_names()
print(ls)


def get_info():
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))
    info = {'name': name, 'age':age}
    return info

myinfo = get_info()

print(myinfo.items())
