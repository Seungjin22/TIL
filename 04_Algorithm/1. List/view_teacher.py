import sys
sys.stdin = open("view_input.txt", "r") # 읽기
sys.stdout = open("view_output.txt", "w") # 쓰기(결과물 파일 만들어줌)
#위 세 줄은 제출할 땐 삭제해줘야!!

T = 10

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

   ans = 0

   for i in range(2, N-2):
       min = 987654321
       for j in range(5):
           if j != 2:
               if data[i]-data[i-2+j] < min:
                   min = data[i] - data[i-2+j]

        if min > 0:
            ans += min

    print("#{} {}".format(tc+1, ans))