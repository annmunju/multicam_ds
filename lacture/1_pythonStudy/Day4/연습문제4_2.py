# 숫자만 추출해서 합계 구하기

str_data = "{a1:20},{a2:30},{a3:15},\
            {a4:50},{a5:-14},{a6:15},\
            {a7:20},{a8:70},{a9:-100}"

first = str_data.split(',')
# print(first)
# ['{a1:20}', '{a2:30}', '{a3:15}', '            {a4:50}', '{a5:-14}', '{a6:15}', '            {a7:20}', '{a8:70}', '{a9:-100}']

second = []
for i in first :
    second.append(i.strip())
# print(second)
# ['{a1:20}', '{a2:30}', '{a3:15}', '{a4:50}', '{a5:-14}', '{a6:15}', '{a7:20}', '{a8:70}', '{a9:-100}']

third = []
for j in second:
    j1 = j.strip('{')
    j2 = j1.strip('}')
    j3 = third.append(j2.split(':'))
# print(third)
# [['a1', '20'], ['a2', '30'], ['a3', '15'], ['a4', '50'], ['a5', '-14'], ['a6', '15'], ['a7', '20'], ['a8', '70'], ['a9', '-100']]

sum = 0

for x in third:
    sum += int(x[1])
print(f'총 합계 : {sum}')