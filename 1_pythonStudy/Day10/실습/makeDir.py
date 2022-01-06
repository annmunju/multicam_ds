
import os
import shutil

# os.mkdir('log')
# shutil.rmtree('log')

# 기존 디렉터리 확인

import os.path

# os.mkdir('log') # 기존에 생성된 폴더를 또 생성하려 할 때 에러 발생
if not os.path.isdir('log'):
    os.mkdir('log')