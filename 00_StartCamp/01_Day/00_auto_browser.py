import webbrowser

searching = ['구미맛집', '구미가볼곳', '구미마트', '구미다이소']

for mysearch in searching:
    print(mysearch)
    webbrowser.open('https://search.naver.com/search.naver?query=' + mysearch)

