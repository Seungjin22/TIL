#1. 각각의 라인을 리스트의 요소로 불러오기
with open('writelines_ssafy.txt', 'r') as f:
    lines = f.readlines()

#2. 뒤집기
lines.reverse()

#3. line을 작성하기
with open('reverse_ssafy.txt', 'w') as f:
    for line in lines:
        f.write(line)