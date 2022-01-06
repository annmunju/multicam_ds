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

dog1 = Dog('','Large',5,'Black')
dog1.setBreed('Neapolitan Mastiff')
dog1.printInfo('첫번째 멍멍이',1)

print('-'*30)

dog2 = Dog('','Small',2,'White')
dog2.setBreed('Maltese')
dog1.printInfo('두번째 멍멍이',2)

print('-'*30)

dog3 = Dog('','Midium',3,'Brown')
dog3.setBreed('Chow Chow')
dog1.printInfo('세번째 멍멍이',3)