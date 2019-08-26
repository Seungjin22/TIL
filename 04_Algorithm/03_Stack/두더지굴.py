import sys
sys.stdin = open('두더지.txt')

def digdug(i, j, N):
    global flag
    data[i][j] = -1
    for id in range(4):
        i = i+dx[id]
        j = j+dy[id]
        if data[i][j] == 0:
            flag = 1
            return
        if i >= 0 and i <= N and j >= 0 and j <= N:
            if data[i][j] == 1:
                digdug(i, j, N)

N = int(input())

data = []
for i in range(N):
    d = list(map(int, input().split()))
    data.append(d)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

flag = 0
for i in range(N):
    for j in range(N):
        if data[i][j]:
            digdug(i, j, N)
