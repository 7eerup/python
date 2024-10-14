from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

from openpyxl import load_workbook
from openpyxl.drawing.image import Image
import requests
from io import BytesIO

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 웹 사이트 열기
driver.get('https://www.naver.com')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()   # 쇼핑 탭 클릭
time.sleep(2)

# 쇼핑 창 실행 후 그 창으로 이동
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
driver.maximize_window()

search = driver.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

search.send_keys("후드 티")
search.send_keys(Keys.ENTER)

before_h = driver.execute_script("return window.scrollY")

while True:
    driver.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)    # 스크롤 바 자동 실행
    time.sleep(1)
    after_h = driver.execute_script("return window.scrollY")    # 이동 후 스크롤 위치
    if after_h == before_h: # 만약에 옮기기 전과 후의 스크롤 위치가 동일하다면
        break
    before_h = after_h

items = driver.find_elements(By.CSS_SELECTOR, ".product_item__MDtDF")

for item in items:
    # 상풍명
    names = item.find_elements(By.CSS_SELECTOR, ".product_title__Mmw2K")
    name = names[0].text if names else "이름 없음"

    # 가격
    prices = item.find_elements(By.CSS_SELECTOR, ".price_num__S2p_v")
    price = prices[0].text if prices else "가격 없음"

    # 링크 찾기
    links = item.find_elements(By.CSS_SELECTOR, ".product_title__Mmw2K > a")
    link = links[0].text if links else "링크 없음"

    # 리뷰 갯수
    review_totals = item.find_elements(By.CSS_SELECTOR, ".product_num__fafe5")
    review_total = review_totals[0].text if review_totals else "리뷰 없음"

    # 이미지 찾기
    images = item.find_elements(By.CSS_SELECTOR, ".thumbnail_thumb__Bxb6Z > img")
    image = images[0].get_attribute('src') if images else "이미지 없음"

    product_info = {
        '상품명': name,
        '가격': price,
        '링크': link,
        '리뷰 수': review_total,
        '이미지': image,
    }

    print(product_info)

driver.quit()