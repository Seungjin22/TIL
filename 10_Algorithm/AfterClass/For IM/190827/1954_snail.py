import sys
sys.stdin = open('1954_input.txt')

def solve(arr):
    global N
    X, Y = 0, 0
    newX, newY = 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_stat = 0
    num = 1
    for i in range(N*N):
        X, Y = newX, newY
        arr[Y][X] = num
        newX = X + dx[dir_stat]
        newY = Y + dy[dir_stat]

        if newY >= N or newX >= N or newY < 0 or newX < 0 or arr[newX][newY] != 0:
            dir_stat = (dir_stat + 1) % 4
            newX = X +dx[dir_stat]
            newY = Y + dy[dir_stat]

        num += 1