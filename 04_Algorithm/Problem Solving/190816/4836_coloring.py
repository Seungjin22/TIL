import sys
sys.stdin = open("4836_input.txt")

T = int(input())


for test_case in range(1, T+1):
    N = int(input())
    square = [[0 for _ in range(1000)] for _ in range(1000)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for h in range(c1, c2 + 1):
            for w in range(r1, r2 + 1):
                square[w][h] += color

                if square[w][h] >= 3:
                    count += 1

    print('#{} {}'.format(test_case, count))




# 선생님 풀이

for test_case in range(1, T+1):
    data = [[0] * N for i in range(N)]
    n = int(input())
    cnt = 0

    for k in range (n):
        r1, c1, r2, c2, color = map(int, input().split())