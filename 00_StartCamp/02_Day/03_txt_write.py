#1. 파일 쓰기(옛날 방식)

# f = open('ssafy.txt', 'w')
# for i in range(10):
#     f.write(f'This is line {i}.\n')
# f.close()  #파일을 열었으면 닫아줘야지! 이거 반드시 반드시 해주기

#2. 파일 쓰기(최신 방식)

with open('with_ssafy.txt', 'w') as f:       #with 구문 이용한 파일 쓰기
    for i in range(10):
        f.write(f'This is line {i}.\n')      #f.close() 쓰지 X