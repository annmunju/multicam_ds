# 상속
# 부모 클래스
# 자식 클래스

class Car :
    speed = 0
    color = ''

    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def drive(self):
        print(f'{self.speed} 속도로 주행합니다.')

    def loading(self):
        print(f'최대 적재량 : {self.load}')


class Truck(Car) :

    def __init__(self, speed, color, load):
        super().__init__(speed, color)
        self.load = load

truck1 = Truck(10, 'red', 1000)
truck1.drive()
truck1.loading()

# vehicle 클래스

class Vehicle(Car):

    def __init__(self, speed, color, seat):
        super().__init__(speed, color)
        self.seat = seat


vehicle1 = Vehicle(20, 'blue', 10)
vehicle1.drive()


