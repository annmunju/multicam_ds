# 상속관계와 포함관계

class Person:

    def __init__(self, name):
        self.name = name

    def greetion(self):
        print('Hi')

    def getName(self):
        print(self.name)

class Student(Person):
    def study(self):
        print('Study')

class PersonList:
    def __init__(self):
        self.personList = []

    def appendPerson(self, person):
        self.personList.append(person.name)

    def printInfo(self):
        for p in self.personList:
            print(p)

personL = PersonList()
for _ in range(3):
    p = Person(input('이름 입력:'))
    p.getName()
    personL.appendPerson(p)

personL.printInfo()