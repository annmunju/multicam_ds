import os

for dirName, subDir, fnames in os.walk('../Day10'):
    for fname in fnames:
        print(f'{dirName}/{fname}')

# 파일 또는 디렉터리 존재 여부 확인

import os.path

print(os.path.exists('../Day10'))
print(os.path.exists('../Day11'))
print(os.path.exists('../Day10/file1.txt'))

# 디렉터리인지 파일인지 구분
print(os.path.isdir('../Day10'))
print(os.path.isfile('../Day10/file1.txt'))