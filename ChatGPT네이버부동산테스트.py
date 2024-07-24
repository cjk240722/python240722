import requests
from bs4 import BeautifulSoup

# 테스트를 위해서 만들었는데 실제로는 되지 않음


# URL 설정 (네이버 부동산 동대문구 매물 페이지 URL)


url = "https://land.naver.com/article/dong/2020024"  # 예시 URL, 실제 URL로 변경 필요

# 웹 페이지 요청 및 응답 받기
try:
    response = requests.get(url)
    response.raise_for_status()  # 요청이 성공적으로 완료되었는지 확인
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 매물 요소 찾기 (예시 CSS 셀렉터, 실제 페이지 구조에 따라 변경 필요)
listings = soup.find_all("div", class_="item_inner")

# 파일 열기 및 매물 정보 추출 및 저장
with open("dongdaemun_listings.txt", "w", encoding="utf-8") as f:
    for listing in listings:
        # 제목, 가격, 주소 정보 추출
        titleElem = listing.find("span", class_="title")
        priceElem = listing.find("span", class_="price")
        addrElem = listing.find("span", class_="address")

        # 요소가 존재하는지 확인
        if titleElem and priceElem and addrElem:
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            addr = addrElem.text.strip()

            # 콘솔에 출력 및 파일에 저장
            print(f"{title}, {price}, {addr}")
            f.write(f"{title}, {price}, {addr}\n")