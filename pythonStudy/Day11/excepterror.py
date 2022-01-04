try :
    num = int(input('숫자 입력:'))

except ValueError as e:
    print('숫자가 아닙니다.',e)

try :
    f = open('text.txt', 'r')
except FileNotFoundError:
    pass
else :
    data = f.read()
    print(data)
    f.close()
finally:
    print('End-----')