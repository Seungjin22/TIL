import sys
sys.stdin = open('0823_workshop.txt')

def start(N):
    for i in range(N):
        for j in range(N):
            if data[i][j] == 2:
                return i, j

def mazerunner(i, j):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    data[i][j] = 2
    if result[0] == 1:
        return
    for idx in range(4):
        if data[i+dx[idx]][j+dy[idx]] == 3:
            result[0] = 1
        elif data[i+dx[idx]][j+dy[idx]] == 0:
            mazerunner(i+dx[idx], j+dy[idx])

for _ in range(10):
    tc = int(input())
    data = []
    for _ in range(16):
        d = list(map(int, input()))
        data.append(d)

    result = [0]
    si, sj = start(16)
    mazerunner(si, sj)

    print('#{} {}'.format(tc, result[0]))


