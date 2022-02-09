from bs4 import BeautifulSoup
import urllib.request  # urllib : 파이썬 내장 모듈


resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver#')
# print(resp)


soup = BeautifulSoup(resp, 'html.parser')
# print(type(soup))


# .lst_dsc>.tit>a 에 있는 텍스트
movies = soup.find_all('dl', class_='lst_dsc')

# print(movies[0].find_all('span', class_='num'))

for movie in movies:
    # 제목
    title = movie.find('a').string
    # 별점
    star = movie.find('span', class_='num').get_text()
    print(f'{title} [{star}]')

# .lst_dsc>.star>.info_star>.star_t1>.num 에 있는 텍스트
