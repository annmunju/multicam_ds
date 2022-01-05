# 인스턴스 변수 : 필드
# 클래스 변수 : 여러 인스턴스가 공유할 수 있는 변수

class Car :
    color = ''
    speed = 10
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1
        print(f'현재 {Car.count}번째 자동차가 생성되었습니다.')

car1 = Car()
car2 = Car()
car3 = Car()

car1.speed # 인스턴스 변수 = 필드
car2.speed

# print(Car.count) # 클래스 변수