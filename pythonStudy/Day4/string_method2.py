cities = '인천 대구 대전 부산 울산 청주 춘천'

city = input('도시명 입력 : ')

if cities.find(city) == -1 :
    print('도시 없음!')
else :
    print('도시 있음!')