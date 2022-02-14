# tuple 원소 추가 삭제 변경 불가

# t1 = (1,2,3)
# t2 = 4,5,6
# t3 = tuple([7,8,9])
#
# print(t1, t2, t3, type(t1), type(t2), type(t3))

# tuple을 변경하기 위해서는 리스트로 변환 후 다시 튜플로 변경

# to_list1 = list(t3)
# print(t3)
# to_list1.reverse()
# t3 = tuple(to_list1)
# print(t3)
#
# print(t2.index(5))
# print(t1.count(4))
#
# del t1
# print(t1)

# 슬라이싱, 인덱싱 사용 가능


myTuple = 10, 20, 30
X = list(myTuple)
print(X)
X.append(40)
myTuple = tuple(X)
print(myTuple)

