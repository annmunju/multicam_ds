# 객체지향 프로그래밍 (Object Oriented Programing)

# 객체 : 함수 + 데이터(변수)

# 클래스로 계산기 정의

class Calculator :
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result

cal1=Calculator()
print(type(cal1))
print(cal1.adder(3))
print(cal1.adder(5))
print(cal1.adder(9))

# 클래스 : 객체 만드는 틀. 기본 정보를 담은 코드. 메소드(함수) + 필드(변수)
# 인스턴스 : 클래스로부터 생성된 객체. 실제로 생성되는 객체
