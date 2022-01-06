# 연습문제
# 총점과 평균을 구해서 출력하기

kor = 90
eng = 80
math = 80

sum = kor + eng + math
avg = sum / 3

print('총점: %d, 평균: %.2f' % (sum, avg))
print(format('총점: %d, 평균: %5.2f' %(sum, avg)))
print('총점: {:d}, 평균: {:5.2f}'.format(sum, avg))