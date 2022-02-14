setA = {1,2,3}
print(type(setA))
print(dir(setA))

# ['__and__', '__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__',
# '__init__', '__init_subclass__', '__ior__', '__isub__',
# '__iter__', '__ixor__', '__le__', '__len__', '__lt__',
# '__ne__', '__new__', '__or__', '__rand__', '__reduce__',
# '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__',
# '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
# '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

setB = set()
print(type(setB))

# 집합 : 중복 불가, 입출력 순서 상이, 인덱스 사용 불가
# 추가, 삭제 가능.

setA.remove(10) # 요소 값이 없는 경우 에러
setA.discard(10) # 요소 값이 없는 경우에도 에러 발생하지 않음

