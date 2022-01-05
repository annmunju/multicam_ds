# Dog Class 에서
# 1. 디폴트 매개변수를 갖는 생성자 정의 (breed는 비공개필드)
# 2. 필드 값을 가져오고, 변경하는 메서드 정의
# 3. sleep(), sit(), run(), eat() 메소드의 내용을 정의
#    출력문으로 '잠자기', '앉다', '뛰다', '먹다'
# 5. 인스턴스를 생성하되, 인수의 수를 다양하게 입력하여 생성
# 6. 인스턴스를 이용하여 개의 정보를 출력하기

class Dog:

    # 1. 디폴트 매개변수를 갖는 생성자 정의
    def __init__(self, breed='', size='Small', age=0, color='white'):
        self.__breed = breed
        self.size = size
        self.age = age
        self.color = color

    # 2. 필드 값을 가져오고, 변경하는 메서드 정의
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

    # 3. sleep(), sit(), run(), eat() 메소드의 내용을 정의
    def eat(self):
        return '먹는 중'
    def sleep(self):
        return '자는 중'
    def sit(self):
        return '앉아 있음'
    def run(self):
        return '뛰는 중'

dog1 = Dog('Large',5,'Black')
dog1.setBreed('Neapolitan Mastiff')
print(f'dog1의 품종 : {dog1.getBreed()}')
print(f'dog1의 나이 : {dog1.getAge()}')
print(f'dog1의 색상 : {dog1.getColor()}')
print(f'dog1의 크기 : {dog1.getSize()}')
print(f'dog1은 지금 {dog1.eat()}')

print('-'*30)

dog2 = Dog('Small',2,'White')
dog2.setBreed('Maltese')
print(f'dog2의 품종 : {dog2.getBreed()}')
print(f'dog2의 나이 : {dog2.getAge()}')
print(f'dog2의 색상 : {dog2.getColor()}')
print(f'dog2의 크기 : {dog2.getSize()}')
print(f'dog2은 지금 {dog2.run()}')

print('-'*30)

dog3 = Dog('Midium',3,'Brown')
dog3.setBreed('Chow Chow')
print(f'dog3의 품종 : {dog3.getBreed()}')
print(f'dog3의 나이 : {dog3.getAge()}')
print(f'dog3의 색상 : {dog3.getColor()}')
print(f'dog3의 크기 : {dog3.getSize()}')
print(f'dog3은 지금 {dog3.sit()}')