# 클래스 구현 과정
# 1) 클래스 정의(선언)
# 2) 객체 생성(인스턴스 생성) = 변수 선언과 비슷
# 3) 객체이용, 메소드, 필드값 변경, 필드값 사용

# class 클래스명:
#     def __init__(self):
#         self.필드명1 = 초기값
#         self.필드명2 = 초기값
#
#     def 메소드명1(self, 매개변수, ...):
#         pass
#
#     # 메소드 정의는 함수 정의와 동일하다.

# -----

# 자동차 클래스
# 기능(동작) => 메소드(함수) : 주행하다, 회전하다
# 속성(상태, 값) => 변수 : color, price, model, seats

# 1) 클래스 정의
class Car:
    def __init__(self):
        self.color = 'red'
        self.speed = 0

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

myCar = Car()
yourCar = Car()

# 2) 객체(인스턴스) 생성
myCar.speedUp()

#인스턴스 생성 후 필드 추가
myCar.color = 'black'
myCar.speed = 100
myCar.speedUp()

# 3) 객체(인스턴스) 사용
print(isinstance(myCar, Car))

print(myCar.speed)