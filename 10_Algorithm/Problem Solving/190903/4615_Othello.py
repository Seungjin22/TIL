import sys
sys.stdin = open('4615_input.txt')

def play(x, y, col):
    x = x-1
    y = y-1
    board[x][y] = col
    dx = [-1, -1, -1, 0, 1, 1, 1, 0]
    dy = [-1, 0, 1, 1, 1, 0, -1, -1]
    for idx in range(8):
            a = x + dx[idx]
            b = y + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= N: continue
            if board[a][b] != col and board[a][b] != 0:
                while True:
                    flag = 0
                    a += dx[idx]
                    b += dy[idx]
                    if a < 0 or a >= N or b < 0 or b >= N: break
                    if board[a][b] == col:
                        while True:
                            a -= dx[idx]
                            b -= dy[idx]
                            if board[a][b] == col:
                                flag = 1
                                break
                            board[a][b] = col
                    elif board[a][b] == 0: break
                    if flag:
                        break

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2-1][N//2] = 1
    board[N//2][N//2-1] = 1
    board[N//2][N//2] = 2
    for _ in range(M):
        x, y, col = map(int, input().split())
        play(x, y, col)
    black = 0
    white = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc, black, white))