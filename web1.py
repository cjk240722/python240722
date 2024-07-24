#web1.pyp

from bs4 import BeautifulSoup

#페이지를 로딩(메소드 체인)
page = open("Chap09_test.html", "rt", encoding="utf-8").read()
#검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser") #html태그를 가지고 있으면 hhtml.parser 
print(soup.prettify()) #전체문자를 출력해줘

#<p> 전체 검색
# print(soup.find_all("p"))

#첫번째 <p>
# print(soup.find("p"))

#조건 : <p class = 'outer-text'>
# print(soup.find_all("p", class_="outer-text"))
# print(soup.find_all("p", attrs={}"class":"outer-text"))
#id = first

# print(soup.find_all(id="first"))

#내부 문자열 출력
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = titile = title.replace("\n", "")
    print(title)