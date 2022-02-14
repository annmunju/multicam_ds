# 여러 클래스에서 상송 받음

class 클래스이름(부모클래스1, 부모클래스2, ...):
    pass

class Person:
    def __init__(self, name = '', age = 0):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'안녕하세요 {self.name}')

class University:
    def __init__(self, department = '', grade = ''):
        self.department = department
        self.grade = grade

    def manageScore(self):
        print('학점관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')