import requests
from bs4 import BeautifulSoup

def crawl_naver_blog(search_keyword):
    # 검색어를 URL 인코딩
    search_url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={requests.utils.quote(search_keyword)}"

    # 검색 결과 페이지 요청
    response = requests.get(search_url)
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return

    # BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.text, 'html.parser')

    # 블로그 검색 결과 추출
    blogs = soup.select("div.api_txt_lines.total_tit")
    for blog in blogs:
        title = blog.text
        link = blog['href']
        
        # 블로그 상세 페이지 요청
        blog_response = requests.get(link)
        if blog_response.status_code != 200:
            continue
        
        blog_soup = BeautifulSoup(blog_response.text, 'html.parser')

        # 블로그명, 포스팅 날짜 추출
        try:
            blog_name = blog_soup.select_one("meta[property='og:site_name']")['content']
        except TypeError:
            blog_name = "Unknown"
        
        try:
            post_date = blog_soup.select_one("meta[property='article:published_time']")['content']
        except TypeError:
            post_date = "Unknown"

        print(f"블로그명: {blog_name}")
        print(f"블로그주소: {link}")
        print(f"제목: {title}")
        print(f"포스팅날짜: {post_date}")
        print("-" * 30)

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    crawl_naver_blog(search_keyword)
