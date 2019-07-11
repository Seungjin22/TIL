from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')  #render_template() 함수

@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name) #template에서 greeting.html 파일 찾아서 열어줌

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html', result=result, number=number)

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '비스트', '기생충', '마담 싸이코', '알라딘', '라이온킹']
    return render_template('movie.html', movies=movies)

# Ping Pong 주고받기
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)

# NAVER 검색 연결하기
@app.route('/naver')
def naver():
    return render_template('naver.html')

# Google 검색 연결하기
@app.route('/google')
def google():
    return render_template('google.html')