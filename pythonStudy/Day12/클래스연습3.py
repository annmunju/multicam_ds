
class Car :
    def __init__(self, speed = 0, color = 'white', modelN=''):
        self.speed = speed
        self.__color = color
        self.modelN = modelN

    def __modelN(self):
        print(self.modelN)

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def printInfo(self):
        self.__modelN()
        print(self.getColor())

    def speedUp(self, sdUp):
        self.speed += sdUp

    def speedDown(self, sdDn):
        self.speed -= sdDn

myCar = Car(speed=100)

import random

for _ in range(10):
    randomNum = random.randint(1, 2)
    if randomNum == 1:
        myCar.speedUp(10)
    else :
        myCar.speedDown(10)

print(myCar.speed)
