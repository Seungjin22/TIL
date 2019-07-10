import requests
from bs4 import BeautifulSoup
from datetime import datetime

html = requests.get('https://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')
tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')

for tag in tags:
    print(tag.text)

now = datetime.now()
with open('naver.txt', 'w', encoding = 'utf-8') as f:
    f.write(f'{now} 기준 네이버 실시간 검색어\n')
    for idx, tag in enumerate(tags):    #enumerate()는 인덱스까지 꺼내주는. idx 자료형 '튜플'
        f.write(f'{idx+1}위: {tag.text}\n')