# 리스트 연산
# + * (반복), 내용 변경

a = [1, 2, 3, 4, 5]

a[1] = '안녕!'
print(a)

a[2:4] = [100,200]

print(a)

# 리스트 복사
b = a # 주소를 참조. 얕은 복사(실제 리스트가 복사되는 것이 아니라 참조값만 복사됨. 원본 함께 수정됨) = shallow copy
a[1] = 2
print(a)
print(b)

# 그럼 깊은 복사는? deep copy
c = list(a)
a[1] = 'hi!'
print(a, c)

import copy
d = ['a', 'b', 'c']
e = copy.deepcopy(d)
print(d,e)
e[0] = 1
print(d,e)
