# 1. 객체간 크기를 비교하는 메서드 작성
# 2. 객체간 나이를 더하고 빼고 곱하고 나누는 메서드 작성

class Dog:

    def __init__(self, length=0, breed='', size='Small', age=0, color='white'):
        self.__breed = breed
        self.size = size
        self.age = age
        self.color = color
        self.length = length

    def getBreed(self):
        return self.__breed
    def setBreed(self, breed):
        self.__breed = breed
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color

    def eat(self):
        return '먹는 중'
    def sleep(self):
        return '자는 중'
    def sit(self):
        return '앉아 있음'
    def run(self):
        return '뛰는 중'

    def printInfo(self,name='개',doing=0):
        print(f'{name}의 품종 : {self.getBreed()}')
        print(f'{name}의 나이 : {self.getAge()}')
        print(f'{name}의 색상 : {self.getColor()}')
        print(f'{name}의 크기 : {self.getSize()}')
        if doing == 1 :
            print(f'{name}은(는) 지금 {dog1.eat()}')
        elif doing == 2 :
            print(f'{name}은(는) 지금 {dog1.sleep()}')
        elif doing == 3 :
            print(f'{name}은(는) 지금 {dog1.sit()}')
        elif doing == 4:
            print(f'{name}은(는) 지금 {dog1.run()}')
        else :
            print(f'{name} 상태 모름')

    # 1. 객체간 크기를 비교하는 메서드 작성

    def __gt__(self, other):
        return self.length > other.length
    def __lt__(self, other):
        return self.length < other.length
    def __ge__(self, other):
        return self.length >= other.length
    def __le__(self, other):
        return self.length <= other.length
    def __ne__(self, other):
        return self.length != other.length
    def __eq__(self, other):
        return self.length == other.length

    # 2. 객체간 나이를 더하고 빼고 곱하고 나누는 메서드 작성

    def __add__(self, other):
        return self.age + other.age
    def __sub__(self, other):
        return self.age - other.age
    def __mul__(self, other):
        return self.age * other.age
    def __truediv__(self, other):
        return self.age / other.age

dog1 = Dog(10,age=5)
dog2 = Dog(20,age=3)

print(f'나이 합산 : {dog1+dog2}')
print(f'나이 차이 : {dog1-dog2}')
print(f'나이 곱 : {dog1*dog2}')
print(f'나이 나눗셈 : {dog1/dog2:.2f}')

if dog1>dog2:
    print('dog1이 dog2보다 크다.')
elif dog1<dog2:
    print('dog2가 dog1보다 크다.')
elif dog1==dog2:
    print('dog1과 dog2는 같다.')