def my_url(itemPerPage=10, **api):
    if 'key' not in api or 'targetDt' not in api:
        return '필수 요청 변수가 누락되었습니다.'
    
    if itemPerPage not in range(1, 11):
        return '1~10까지의 값을 넣어 주세요.'
    
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
    base_url += f'itemPerPage={itemPerPage}'
    for key, value in api.items():
        base_url += f'{key}={value}&'
    return base_url