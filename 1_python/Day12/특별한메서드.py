# __메서드이름__ : 이미 정의된 메서드

# __ge__() : >=
# __gt__() : >
# __lt__() : <
# __le__() : <=
# __ne__() : !=
# __eq__() : ==

# __init__() : 생성자
# __repr__() : 인스턴스 print()문으로 출력
# __add__() : +
# __del__() : 소멸자, 인스턴스 삭제

# 선 클래스 : (필드) 길이, 색상, 두께 / (메서드) 더하기, 크기비교

class Line:

    def __init__(self, length = 0):
        self.length = length
        print(f'{self.length} 길이의 선분이 생성되었습니다.')

    def __add__(self, other):
        return self.length + other.length

    def __gt__(self, other):
        return self.length > other.length

line1 = Line(10)
line2 = Line(5)
print('line1 :',line1.length)
print('line2 :',line2.length)

print('line1+line2 :',line1+line2) # __add__가 실행됨
# print('line1-line2 :',line1-line2) : 정의되지 않아서 호출되지 않음