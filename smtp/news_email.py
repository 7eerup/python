from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 웹 사이트 열기
driver.get('https://news.google.com')
time.sleep(1)

driver.maximize_window()
time.sleep(2)

SEARCH_KEYWORD = '전기 자동차'

search_bar = driver.find_element(By.CSS_SELECTOR, '.Ax4B8.ZAGvjd')
search_bar.click()
search_bar.send_keys(SEARCH_KEYWORD)
search_bar.send_keys(Keys.ENTER)

time.sleep(3)

before_h = driver.execute_script("return window.scrollY")
while True:
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
    time.sleep(1)
    after_h = driver.execute_script("return window.scrollY")
    if after_h == before_h:
        break
    before_h = after_h

data_list = []

article_list = driver.find_elements(By.CSS_SELECTOR, '.JtKRv')

for article in article_list:
    title = article.text
    link = article.get_attribute('href')

    data_dict = {'title': title, 'link': link}
    data_list.append(data_dict)
    print(title)

print(data_list)

driver.quit()