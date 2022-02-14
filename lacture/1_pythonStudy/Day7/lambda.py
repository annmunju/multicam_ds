'''
# 람다 함수 한줄로 쓰기

def add(x, y):
    result = x + y
    return result

print(add(10, 20))

add2 = lambda x,y : x+y

print(add2(10, 20))

# 리스트의 각 요소에 10을 더하는 함수
def add10(nums):
    ls = []
    for n in nums:
        ls.append(n+10)
    return ls

def addTen(num):
    return num + 10

nums = [1,2,3,7]
for n in range(len(nums)):
    nums[n] = addTen(nums[n])

print(nums)

# map() 함수
num2 = list(map(addTen, nums))
print(num2)

# lambda + map
num3 = list(map(lambda num : num+10, num2))

print(num3)

X = (lambda x : x+10)(25)
print(X)

# Y = (lambda x : y=10; x+y)(5) : 람다 표현식 안에서 변수 생성 불가

y=10
New = (lambda x : x+y)(5)
print(New)
'''

# 문제2. 두 리스트의 각 자리수 값을 합해서 새로운 리스트 생성
list1 = [1,2,3,4]
list2 = [10,20,30,40]

def addList(x,y):
    ls = []
    for i in range(len(x)):
        ls.append(x[i] + y[i])
    return ls

print(addList(list1, list2))

# lambda & map 사용
mapX = list(map(lambda x,y : x+y, list1, list2))
print(mapX)