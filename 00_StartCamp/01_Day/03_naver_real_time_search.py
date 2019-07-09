import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
names = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')    #실시간 검색어는 여러개. 뱉어내는게 list
#print(type(names))   #>>> list
'''
for name in names:
    print(name.text)
'''  #읽지 않는 스트링으로 만들기 (주석은 X)

for idx, name in enumerate(names):     #enumerate는 인덱스 번호까지 같이 뺴내주는 함수
    print(f'{idx+1}위: {name.text}')