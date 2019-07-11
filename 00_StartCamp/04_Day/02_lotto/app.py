from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests, random

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    num = request.args.get('num')
    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866')
    lotto = res.json() 

    #1. 번호 6개 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    #2. 내 번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))

    if len(numbers) == 6:
        # 번호 교집합 개수 찾기
        matched = 0
        for num in numbers:
            if num in winner:
                matched += 1
        if matched == 6:
            result = '축하합니다~ 1등입니다!!! 퇴사하세요^^'
        elif matched == 5:
            if lotto['bnusNo'] in numbers:
                result = '2등입니다. 보너스 숫자 잘고르셨네요.'
            else:
                result = '3등입니다. 아깝네요. 그래도 이게 어딘가요.'
        elif matched == 4:
            result = '4등입니다. 택시비 나왔네요.'
        elif matched == 3:
            result = '5등입니다. 이번엔 숫자 잘 골라보세요.'
        else:
            result = '꽝 입니다. 돈 날리셨네요!'
    else:
        result = '번호의 수가 6개가 아닙니다.'

    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)