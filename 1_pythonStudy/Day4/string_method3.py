# cities = '인천 대구 대전 부산 울산 청주 춘천'
#
# cities_split = cities.split()
# print(cities_split)

birth = input('생일 입력(연/월/일) : ')
birth_split = birth.split('/')

print(f'당신은 {birth_split[0]}년에 태어났고\n생일은 {birth_split[1]}월 {birth_split[2]}일 이군요')