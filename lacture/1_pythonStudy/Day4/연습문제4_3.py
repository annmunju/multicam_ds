# 하트 출력

heart = input('숫자를 여러개 입력하세요.')

for i in heart:
    heart_num = int(i)
    print('\u2665'*heart_num)

print("%10s" % "파이썬")