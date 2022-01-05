# 생성자 : 객체(인스턴스) 생성하면서 필드값을 초기화하는 함수
# class 클래스명:
#     def __init__(self, *args):
        # 이 부분에 필드 초기화 코드 입력

# self : 클래스에서 생성된 인스턴스에 접근.
# 인스턴스가 생성된 후에 해당 인스턴스 이름으로 값을 할당하거나 메서드 호출

# __ : 특수한 예약함수(메소드), 변수에 사용


# _ : 변수를 이름 없이 사용하기 위해
for _ in range(10):
    print('!',end = ' ')
print()

class Car :
    def __init__(self):
        self.speed = 0
        self.color = 'red'

car1 = Car()
print(f'자동차 색상 : {car1.color}')
print(f'자동차 속도 : {car1.speed}')


class Car1 :
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

myCar = Car1(100,'black')
print(f'자동차 색상 : {myCar.color}')
print(f'자동차 속도 : {myCar.speed}')
print(isinstance(myCar, Car1))

class Car2 :
    def __init__(self, speed=0, color='red'):
        self.speed = speed
        self.color = color

yourCar = Car2(50,'yellow')
print(f'자동차 색상 : {yourCar.color}')
print(f'자동차 속도 : {yourCar.speed}')
print(isinstance(yourCar, Car2))

class Car3 :
    def __init__(self, speed=0, color='red'):
        self.speed = speed
        self.color = color

    def drive(self) :
        self.speed = 50

    def speedUp(self):
        self.speed += 10

if __init__ == '__main__':
    myCar4 = Car3()
    print('초기 속도', myCar4.speed)
    myCar4.drive()
    print('drive() 수행 후 속도', myCar4.speed)
    myCar4.speedUp()
    print('speedUp() 수행 후 속도', myCar4.speed)