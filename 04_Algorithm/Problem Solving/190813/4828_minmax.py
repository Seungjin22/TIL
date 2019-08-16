
import sys
sys.stdin = open("4828_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    min_num = data[0]
    max_num = data[0]

    for i in range(1, len(data)):
        if data[i] >= max_num:
            max_num = data[i]
        elif data[i] <= min_num:
            min_num = data[i]

    result = max_num - min_num

    print("#{} {}".format(test_case, result))