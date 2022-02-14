# 인스턴스를 통하지 않고 메서드를 클래스에서 바로 불러올(호출할) 수 있는 것

# @classmethod를 메서드 위에 붙임
# : 메서드 내 인수로 cls를 지정
# : cls = class

class Person :
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count+=1

    @classmethod
    def printCount(cls):
        print(f'{cls.count}명 탄생')

man1 = Person('Kim')
man2 = Person('Lee')
Person.printCount()