from datetime import date, datetime, timedelta

today = date.today()
year = today.year
month = today.month
day = today.day
print(datetime.now().minute)

print(f'오늘은 {year}년 {month}월 {day}일 입니다!')

# 날짜 계산 timedelta
a = today + timedelta(days=1)
b = today - timedelta(days=-1)
print(f'{a}\n{b}')

current_time = datetime.now()
print(current_time + timedelta(hours=-1))

# strftime() 함수 : 날짜 형식을 문자열로 반환
str_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

print(type(current_time), type(str_time))

# strptime() : 문자열을 날짜 형식으로 반환
remember = datetime.strptime("2019-04-26", "%Y-%m-%d")
print(remember - timedelta(days=-3000))