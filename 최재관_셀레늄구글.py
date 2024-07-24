from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#크롬드라이버 실행
driver = webdriver.Chrome()
#url 주소 추가해서 실행
driver.get("https://www.google.co.kr")
#창이 오픈되고 3초를 대기
time.sleep(3) #너무 빠르게 검색하면 안되니까 일부러 3초 딜레이


#검색어창 찾기
searchBox = driver.find_element(By.CLASS_NAME, "gLFyf")


# //현재 계층의 모든 태그 
# XPath

searchBox.send_keys("맥북")
searchBox.send_keys(Keys.RETURN)
time.sleep(10)

#내가 원할때 닫기 위해서 하기 코드 사용
while True:
    pass
