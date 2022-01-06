class Person:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print('Hi')

class Student(Person):
    department = ''
    grade = 0

    def __init__(self, name, age, department, grade):
        super().__init__(name, age)
        self.department = department
        self.grade = grade

    def study(self):
        print('Study')

mj = Student('ann', 26, 'management', 4)
print(type(mj))