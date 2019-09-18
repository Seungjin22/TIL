import sys
sys.stdin = open('5188_input.txt')


def minPath(x, y, rst, N):
    global min
    rst += data[x][y]
    if rst > min: return
    if x == N - 1 and y == N - 1:
        if rst < min:
            min = rst
        return
    for i in range(2):
        a = x + dx[i]
        b = y + dy[i]
        if a < 0 or a >= N or b < 0 or b >= N: continue
        minPath(a, b, rst, N)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1]
    dy = [1, 0]
    min = 987654321
    minPath(0, 0, 0, N)
    print('#{} {}'.format(tc, min))