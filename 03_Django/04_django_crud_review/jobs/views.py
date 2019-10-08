from django.shortcuts import render, redirect
from .models import Job
from faker import Faker
from decouple import config
import requests

def index(request):
    return render(request, 'jobs/index.html')


def past_life(request):
    name = request.POST.get('name')
    person = Job.objects.filter(name=name).first()
    # filter 는 값이 없어도 에러가 나지 않음

    # DB에 이름이 있을 경우
    if person:
        past_job = person.past_job
    # DB에 이름이 없을 경우
    else:
        fake = Faker()
        # 랜덤 직업 생성
        past_job = fake.job()
        # 새로운 이름, 직업 추가 후 DB 저장
        person = Job(name=name, past_job=past_job)
        person.save()

    # GIPHY
    #1. API key 가져오기
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    #2. 요청 URL 세팅
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    #3. 실제 요청을 보내자 (json -> dict)
    data = requests.get(url).json()
    #4. image 추출
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None

    # context = {'person': person, 'image': image}
    # return render(request, 'jobs/past_life.html', context)


    # NAVER IMAGE
    #1. 요청 헤더 정보 준비
    NAVER_ID = config('NAVER_ID')
    NAVER_SECRET = config('NAVER_SECRET')

    headers = {'X-Naver-Client-Id': NAVER_ID,
            'X-Naver-Client-Secret': NAVER_SECRET,}

    #2. 요청 URL 준비
    naver_url = f'https://openapi.naver.com/v1/search/image?query={past_job}&filter=medium&display=1'

    #3. 실제 요청 보내기
    naver_data = requests.get(naver_url, headers=headers).json()
    print(naver_data)

    #4. 이미지 링크 추출하기
    naver_image = naver_data.get('items')[0].get('link')

    context = {'person':person, 'image': image, 'naver_image': naver_image,}

    return render(request, 'jobs/past_life.html', context)

