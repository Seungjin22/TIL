from flask import Flask
import datetime
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/ssafy')
def ssafy():
    return 'This is ssafy!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    endgame = datetime.datetime(2019, 11, 29)
    td = endgame - today
    return f'SSAFY 1학기 종료까지 {td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄로 작성하자!</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<string:name>')
def greeting(name):
    return f'반갑습니다! {name}님'

@app.route('/cube/<int:number>')
def mul(number):
    return f'{number}의 3제곱은 {number**3}입니다.'

# 점심 메뉴 리스트(5개)에서 2개를 뽑아 출력하기
# >>> flask는 문자형만 return. str()으로 감싸서 출력해줘야!

@app.route('/lunch/<int:person>')
def lunch(person):
    menu = ['쇠고기 덮밥', '빨간 우동', '카레 갈치 구이', '테이크아웃']
    td_lunch = random.sample(menu, person)
    return f'오늘의 점심 메뉴는 {td_lunch}입니다.'
