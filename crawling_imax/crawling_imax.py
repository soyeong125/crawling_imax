
import requests
from bs4 import BeautifulSoup #웹 크롤링에 필요한 모듈 설치

url = 'https://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220602' #현재 안됨;; 왜 ㅡㅡ
html = requests.get(url)
print(html.text)


