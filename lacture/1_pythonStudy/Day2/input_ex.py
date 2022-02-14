
# 연습문제 1

kor = int(input('국어점수 입력 : '))
eng = int(input('영어점수 입력 : '))
math = int(input('수학점수 입력 : '))

sum = kor + eng + math
avg = sum / 3

print("총점 : %d" % sum)
print("평균 : %.2f" % avg)

# 연습문제 2 : 몸무게 / (키*키)

weight = int(input('몸무게(kg) : '))
height = float(input('키(미터) : '))

bmi = weight / (height ** 2)

print("당신의 BMI는 %.2f 입니다." % bmi)