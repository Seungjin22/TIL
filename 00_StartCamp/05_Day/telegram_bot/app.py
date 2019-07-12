from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')

    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])   #/{token} 이건 아무나 못 들어오게 랜덤 숫자 주소 뒤에 주는 효과
def telegram():
    #1. 구조 print 해보기 & 변수 저장
    # print(request.get_json())
    # print(type(request.get_json()))
    from_telegram = request.get_json()
    print(from_telegram)

    #2. 메시지를 그대로 돌려 보내기
    if from_telegram.get('message') is not None: #텔레그램에서 수정된 메세지 다시 보내면 none으로 표시됨. 그 경우 제외시키는 것.(예외처리)
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # print(text)
        
        # print(res)

        #3. Keyword(번역)
        if text[0:4] == '/번역 ':
            headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
            data = {'source': 'ko', 'target': 'en', 'text': text[4:]}

            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            print(papago_res.json())
            text = papago_res.json().get('message').get('result').get('translatedText')
            print(text)
        res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
            
    return '', 200