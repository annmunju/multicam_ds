# 문자열 정렬 > < ^(가운데 정렬)
# {:<10} 10자리 왼쪽에 맞춰서 써라
string = 'python'
print('{:-^10}'.format(string))

# ljust(자릿수) : 왼쪽 정렬, rjust() 오른쪽 정렬, center() 가운데 정렬

print(string.center(10, '-'))