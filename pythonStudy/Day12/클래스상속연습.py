# Animal 클래스 정의
# 메서드 talk(), eat(), sleep()
# 필드 age, leg, color, breed

# 서브클래스 Dog 정의
# 메서드 : talk() 재정의 -> '멍멍'
# 필드 추가

# 서브클래스 Cat 정의
# 메서드 : talk() 재정의 -> '야옹'
# 필드 추가

class Animal:
    age=0 ; leg=0
    color='' ; breed=''

    def __init__(self, age, leg, color, breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def talk():
        print('짖는다')

    def eat():
        print('먹는다')

    def sleep():
        print('잔다')

    def printInfo(self, name='알 수 없음'):
        print(f'{name}은 {self.age}살이다.\n'
              f'{self.color} 색상에 {self.breed} 종이다.\n'
              f'먹이는 {self.feed}를 먹는다.')

    def doing(self, inputNum = 0):
        if inputNum == 1 :
            print(self.__class__.__name__,'가', end=' ')
            Animal.talk()
        elif inputNum == 2 :
            print(self.__class__.__name__,'가', end=' ')
            Animal.eat()
        elif inputNum == 3 :
            print(self.__class__.__name__,'가', end=' ')
            Animal.sleep()
        else :
            print(self.__class__.__name__, '가 뭘 하는지 알 수 없다.')

class Dog(Animal):

    def __init__(self, age, leg, color, breed, feed):
        super().__init__(age, leg, color, breed)
        self.feed = feed

    def talk(self):
        print('멍멍')

class Cat(Animal):
    def __init__(self, age, leg, color, breed, feed):
        super().__init__(age, leg, color, breed)
        self.feed = feed

    def talk(self):
        print('야옹')

bori = Cat(4, 4, 'orange', 'korean short hair', 'dry feed')
bori.printInfo('보리')
bori.doing(1)
print('-'*40)
jennifer = Dog(16, 4, 'black', 'poodle', 'Caesar Can')
jennifer.printInfo('제니퍼')
jennifer.doing()
print('-'*40)

# 다형성
animals = [Cat(1, 4, 'white', 'korean long hair','wet food'),
           Cat(2, 4, 'black and white', 'abyssinian','dry food'),
           Dog(5, 4, 'brown', 'bulldog', 'anything')]

animals[1].printInfo('냥이')
animals[2].talk()
animals[0].talk()