# 이메일 판별

email = input("이메일 입력 : ")


if '.' not in email or '@' not in email or '.@' in email or '@.' in email or email.count('.') != 1 or email.count('@') != 1:
    print("이메일 형식이 아닙니다.")
else :
    e_split = email.split('@')
    e_front = e_split[0]
    e_back = e_split[1]
    e_back_split = e_back.split('.')

# @앞에 문자가 없는 경우, 뒤에 뭇자가 없는 경우
    if '' in e_split : print("이메일 형식이 아닙니다.")

# .이 앞에 오는 경우
    elif '.' in e_front: print("이메일 형식이 아닙니다.")

# . 뒤에 문자가 없는 경우
    elif '' in e_back_split : print("이메일 형식이 아닙니다.")

    else : print("이메일 형식이 맞습니다.")

print(f'입력한 이메일 : {email}')