from flask import Flask, render_template, request
import requests, random

app = Flask(__name__)

@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/result')
def result():
    #1. form태그로 날린 데이터를 받는다.
    word = request.args.get('word')

    #2. ARTII api로 (font_list)요청을 보내 받은 응답 결과를 text로 fonts(변수)에 저장
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text

    #3. fonts(str)를 fonts(list)로 바꾼다. >>형변환
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해 font에 담는다.
    font = random.choice(fonts)

    #5. 위에서 우리가 만든 word와 font를 가지고 다시 요청을 보낸다.
    # 요청 결과(응답)를 result에 저장한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    #6. 최종적으로 result에 담긴 문자열을 result.html에서 보여준다.
    return render_template('result.html', result=result)
