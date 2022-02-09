from bs4 import BeautifulSoup
import requests

def pageCrawling(url, page):
    global tit_ls, soup, resp
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')

    learn_search = soup.find('div', {'class': 'result-list'})

    learn_ls = learn_search.find_all('li')

    for learn in learn_ls:
        title = learn.find('span', class_='title').text
        # print(title.strip())
        tit_ls.append(title.strip())

tit_ls = list()
page = 1
url = f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={page}'
pageCrawling(url, page)

pages = soup.find('nav', class_='pagination').find_all()
pg = list()
for page in pages:
    if page.text.isdigit():
        pg.append(page.text)
print(pg)
# 최종 페이지 리스트 : pg

tit_ls = list()
for p in pg:
    page = p
    url = f'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage={page}'
    pageCrawling(url, page)

print(tit_ls)
print(len(tit_ls))