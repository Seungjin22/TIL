#1-1. 파일 읽기(옛날 방식) - read()

# f = open('ssafy.txt', 'r')
# all_text = f.read()     #f.read()는 파일 전체를 문자열로 나타내주는 함수
# print(all_text)
# f.close()


#1-2. 파일 읽기(최신 방식) - read()

# with open('with_ssafy.txt', 'r') as f:
#     all_text = f.read()
#     print(all_text)


#2-1. 파일 읽기(옛날 방식) - readlines() : 라인들을 모두 읽어서 리스트를 만든 후 리스트를 읽음

# f = open('ssafy.txt', 'r')
# lines = f.readlines()     #여기서 변수 lines의 형식은 list!!

# for line in lines:
#     print(lines)
#     print(line)

# f.close()


#2-2. 파일 읽기(최신 방식) - readlines()

with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())   #strip() \n 제거하기 위해 사용 rstrip():오른쪽, lstrip():왼쪽