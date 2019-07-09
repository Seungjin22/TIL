import requests
from bs4 import BeautifulSoup  #bs4라는 모듈에서 BeautifulSoup을 가져와서 쓴다.

url = 'https://finance.naver.com/sise/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser') #파씽한다 : 유용한 정보를 가져온다.
kospi = soup.select_one('#KOSPI_now').text  #id라서 #을 찍음
print(f'오늘의 코스피 지수는 {kospi}입니다.')