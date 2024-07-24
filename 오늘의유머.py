# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,11):
        #오늘의 유머 베스트 게시판
        data ='https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우 디코딩
        page = data.decode('utf-8', 'ignore') #한글이 깨지면 decode하는 것이 필요

        #스프 객체 : 검색을 위한 객체
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={"class":"subject"})


        # <td class="subject"><a href="/board/view.php?table=bestofbest&amp;no=476026&amp;s_no=476026&amp;page=5" target="_top">북한에서 편의점 운영한 썰.jpg</a>
        # <span class="list_memo_count_span"> [23]</span>  
        # <span style="margin-left:4px;"><img src="http://www.todayhumor.co.kr/board/images/list_icon_photo.gif" style="vertical-align:middle; margin-bottom:1px;"> 
        # </span><img src="http://www.todayhumor.co.kr/board/images/list_icon_shovel.gif?2" alt="펌글" style="margin-right:3px;top:2px;position:relative"> </td>

        

        for item in list:
                
                #에러 처리 구문

                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        title = item.find("a").text.strip()
                        # print(title)
                        if (re.search('한국', title)):
                                print(title.strip())
                except:
                        pass
        
