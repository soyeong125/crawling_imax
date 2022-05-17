
import requests
from bs4 import BeautifulSoup #웹 크롤링에 필요한 모듈 설치

url = 'https://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220517' #현재 안됨;; 왜 ㅡㅡ
#url = 'http://www.cgv.co.kr/theaters/?areacode=01&theaterCode=0056&date=20220517' #현재 안됨;; 왜 ㅡㅡ
html = requests.get(url)

soup = BeautifulSoup(html.text, 'html.parser')
title_list = soup.select('div.info-movie')
print(title_list)


