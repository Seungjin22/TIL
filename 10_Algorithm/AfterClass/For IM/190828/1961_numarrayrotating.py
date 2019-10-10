import sys
sys.stdin = open('1961_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]
    for i in range(N):
        data[0][i] = list(map(int, input().split()))

    for n in range(3):
        for i in range(N):
            for j in range(N):
                    data[n+1][j][N-1-i] = data[n][i][j]

    print('#{}'.format(tc))
    for i in range(N):  # 행
        for n in range(1, 4): # 면
            for j in range(N):  # 열
                print(data[n][i][j], end="")
            print(end=" ")
        print()