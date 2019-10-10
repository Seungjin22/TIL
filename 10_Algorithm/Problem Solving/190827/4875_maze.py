import sys
sys.stdin = open('4875_input.txt')

def mazerunner(i, j, N):
    global flag
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    maze[i][j] = 3
    for id in range(4):
        a = i + dx[id]
        b = j + dy[id]
        if a >= 0 and a < N and b >= 0 and b < N:
            if maze[a][b] == 2:
                flag = 1
            if maze[a][b] == 0:
                mazerunner(a, b, N)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        m = list(map(int, input()))
        maze.append(m)

    flag = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                mazerunner(i, j, N)

    print('#{} {}'.format(tc, flag))