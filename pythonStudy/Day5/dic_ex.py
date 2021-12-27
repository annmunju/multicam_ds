data1 = {'name' : '버섯불고기',
        'class' : '한식',
        'type' : '불고기',
        'ingr' : ['버섯', '소고기', '양파', '간장', '설탕']}
data2 = {'name' : '카레덮밥',
        'class' : '양식',
        'type' : '덮밥',
        'ingr' : ['카레', '감자', '양파', '당근']}

datum = [data1, data2]

# 음식정보 출력하기

for data in datum:
        for d in data:
                