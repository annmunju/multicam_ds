'''
import sys

bmodule = sys.builtin_module_names
print(bmodule)

# ('_abc', '_ast', '_codecs', '_collections', '_functools',
# '_imp', '_io', '_locale', '_operator', '_signal', '_sre',
# '_stat', '_string', '_symtable', '_thread', '_tracemalloc',
# '_warnings', '_weakref', 'atexit', 'builtins', 'errno',
# 'faulthandler', 'gc', 'itertools', 'marshal', 'posix',
# 'pwd', 'sys', 'time', 'xxsubtype')

import _string

help(_string.formatter_parser)
'''


import pandas as pd


# 모듈 내에서 __로 시작하는 스패셜변수나 매직메서드를 제외한 모든 것을 참조한다. #

import calculation_module

print(calculation_module.add(1,2))

# show.py 모듈로 활용해보기 : 같은 폴더 안에 있어야 불러오기 가능!

# import sys
# sys.path.append('경로입력')

from show import *

show_name()
show_phone()