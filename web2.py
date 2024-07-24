#web2.py
import requests
from bs4 import BeautifulSoup


url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})






#파일에 저장
# f = open("daanggn.txt", "wt", encoding="utf-8") #덮어쓰기 하니까 문제소지 있음
f = open("daanggn.txt", "a+", encoding="utf-8") #덮어쓰기 하니까 문제소지 있음

for post in posts:

    titleElem = post.find("h2", attrs={"class":"card-title"})
    priceElem = post.find("div", attrs={"class":"card-price"})
    addrElem = post.find("div", attrs={"class":"card-region-name"})

    title = titleElem.text.strip()
    price = priceElem.text.strip()
    addr = addrElem.text.strip()

    print(f"{title}, {price}, {addr}") #f로 포맷을 설정
    f.write(f"{title}, {price}, {addr}\n")
    
# <div class="card-desc">
#       <h2 class="card-title">제습기</h2>
#       <div class="card-price ">
#         9,000원
#       </div>
#       <div class="card-region-name">
#         부산 부산진구 범전동
#       </div>




# urlLand = "https://new.land.naver.com/complexes/117771?ms=37.5871064,127.0508293,16&a=APT&e=RETAIL&ad=true"
# responseLand = requests.get(urlLand)
# soupLand = BeautifulSoup(responseLand.text, "html.parser")
# postsLand = soupLand.find_all("div", attrs={"class":"item_inner"})

# for postLand in postsLand:
#     item_titleLand = postLand.find("div", attr={"class":"item_title"})
#     price_lineLand = postLand.find("div", attr={"class":"price_line"})
#     info_areaLand = postLand.find("div", attr={"class":"info_area"})
    
#     item_title = item_titleLand.text.strip()
#     price_line = price_lineLand.text.strip()
#     info_area = info_areaLand.text.strip()

#     print(f"{item_title}, {price_line}, {info_area}") #f로 포맷을 설정


