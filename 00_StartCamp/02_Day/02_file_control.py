import os

os.chdir(r'C:\Users\student\TIL\00_StartCamp\02_Day\dummy')

for filename in os.listdir('.'):
    #os.rename(filename, f'SAMSUNG_{filename}')      #모든 파일 이름 앞에 SAMSUNG_ 붙이기
    os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))  #SAMSUNG_ 대신 SSAFY_로 바꾸기
    