
# 비공개 필드 (__필드명)
# 필드를 외부에서 직접 사용하지 못하도록 하는 방법

class Car :
    def __init__(self, speed = 0, color = 'white'):
        self.speed = speed
        self.__color = color

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

car1 = Car()
# print(car1.color) : 사용불가!
print(car1.getColor())
car1.setColor('red')
print(car1.getColor())
