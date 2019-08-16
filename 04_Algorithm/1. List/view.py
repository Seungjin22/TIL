import sys
sys.stdin = open("view_input.txt", "r") # 읽기
sys.stdout = open("view_output.txt", "w") # 쓰기(결과물 파일 만들어줌)
#위 세 줄은 제출할 땐 삭제해줘야!!

T = 10

def skyview(arr):
    ans = 0
    for i in range(2, len(arr)-2):
        height = arr[i]
        if arr[i-2] >= arr[i-1]:
            left = arr[i-2]
        else:
            left = arr[i-1]
        if arr[i+1] >= arr[i+2]:
            right = arr[i+1]
        else:
            right = arr[i+2]

        if left >= height or right >= height:
            continue
        else:
            if left >= right:
                ans += (height-left)
            else:
                ans += (height-right)
    return ans

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = skyview(arr)

    print("#{} {}".format(tc+1, ans))