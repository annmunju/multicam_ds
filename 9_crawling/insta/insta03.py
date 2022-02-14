from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

input_id = input('id 입력 : ')
input_pw = input('pw 입력 : ')
tag = '#'+input('검색할 단어 : ')

service = webdriver.chrome.service.Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=service)
url = 'https://www.instagram.com/accounts/login/'
driver.get(url)
sleep(5)

id = driver.find_element(By.NAME, 'username')
id.send_keys(input_id)
pw = driver.find_element(By.NAME, 'password')
pw.send_keys(input_pw)
sleep(2)

driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)").click()
sleep(5)

driver.find_element(By.CLASS_NAME, "cmbtv").click()
sleep(5)

driver.find_element(By.CSS_SELECTOR, ".mt3GC > button:nth-child(2)").click()
sleep(5)

search_tag = driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search_tag.send_keys(tag)
sleep(2)

driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
sleep(1)

url = driver.current_url
print(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div', class_='KL4Bh')

for img in img_list:
    print(img)

