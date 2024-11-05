from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)

# 예시로 Google의 날씨 정보 페이지로 이동
driver.get("https://www.google.com/search?q=weather")

element = driver.find_element(By.ID, "wob_tm").text
loc = driver.find_element(By.CSS_SELECTOR, 'span.BBwThe').text

print(f"현재 {loc}의 온도는 {element}도")