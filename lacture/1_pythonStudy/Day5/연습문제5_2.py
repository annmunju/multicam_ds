diction = {}

keyX = input('영어 단어 등록 (종료는 quit) : ')

while keyX != 'quit':
    if keyX in diction.keys():
        print(f'{keyX}는 이미 등록된 단어 입니다.')
    else :
        valueX = input(f'{keyX}의 뜻입력 (종료는 quit) : ')
        diction[keyX] = valueX
    keyX = input('영어 단어 등록 (종료는 quit) : ')

# -----

searchX = input('검색할 단어 입력 (종료는 quit) : ')

while searchX != 'quit':
    if searchX not in diction.keys():
        print(f'{searchX}는 사전에 없는 단어 입니다.')
    else :
        print(f'{searchX}의 뜻은 {diction[searchX]}입니다.')
    searchX = input('검색할 단어 입력 (종료는 quit) : ')

print('종료합니다.')