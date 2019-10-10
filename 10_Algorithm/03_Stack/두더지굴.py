import sys
sys.stdin = open('두더지.txt')

def digdug(i, j, color):
    visited[i][j] = color
    for id in range(4):
        a = i+dx[id]
        b = j+dy[id]
        if a >= 0 and a < N and b >= 0 and b < N:
            if visited[a][b] == 0 and data[a][b] == 1:
                digdug(a, b, color)

N = int(input())

data = []
for i in range(N):
    d = list(map(int, input().split()))
    data.append(d)
visited = [[0 for _ in range(N)] for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 1 and visited[i][j] == 0:
            ans += 1
            digdug(i, j, ans)
            count[0] += 1


print(visited)