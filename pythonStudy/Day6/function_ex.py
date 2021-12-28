
# 상품 가격, 주문 수량 입력받아서

def order():
    price = int(input('상품 가격 입력 : '))
    count = int(input('주문 수량 입력 : '))
    result = price*count
    return price, count, result

price, count, result = order()

print('-'*20)
print(f'상품 가격 : {format(price, ",")}원')
print(f'주문 수량 : {format(count, ",")}원')
print(f'주문액 : {format(result, ",")}원')


# 사칙연산 함수 작성

def inputNum():
    num1 = int(input('숫자 1 입력 : '))
    num2 = int(input('숫자 2 입력 : '))
    return num1, num2

def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    result = num1 / num2
    return result

def mod(num1, num2):
    result = num1 % num2
    return result

a , b = inputNum()

print(f'{a} + {b} = {add(a, b)}')
print(f'{a} - {b} = {sub(a, b)}')
print(f'{a} * {b} = {mul(a, b)}')
print(f'{a} / {b} = {div(a, b)}')
print(f'{a} % {b} = {mod(a, b)}')



def order(price, qt):
    amount = price * qt
    if amount >= 100000:
        discount = amount*0.1
    elif amount >= 50000:
        discount = amount*0.05
    else:
        discount = 0
    result = amount - discount
    return amount, discount, result

price = int(input('상품 가격 입력 : '))
qt = int(input('주문 수량 입력 : '))
amount, discount, result = order(price, qt)

print(f'주문액 : {amount}')
print(f'할인액 : {discount}')


# 디폴트 매개변수. def 변수명(a, b=1, c=2)~ b, c는 작성 안해놓으면 디폴드값으로 적용됨.