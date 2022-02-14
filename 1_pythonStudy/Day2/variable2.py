# 화씨 온도를 섭씨 온도로 변환하기

fTemp = 80
cTemp = (fTemp - 32) * 5 / 9

print(cTemp)

# 포메팅
print('%f' % cTemp) # 소수점 이하 6자리
print('%.2f' % cTemp)
print('%6.2f' % cTemp)

print(format(cTemp ,'.2f'))
print(format(cTemp ,'6.2f'))

# 2개 이상 값 출력
print('%d\t%f' % (fTemp, cTemp))