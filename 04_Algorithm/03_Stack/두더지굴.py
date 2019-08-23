import sys
sys.stdin = open('두더지.txt')

def digdug(i, j):
    for id in range(4):
        i = i+dx[id]
        j = j+dy[id]
        if i >= 0 and i <


N = int(input())

data = []
for i in range(N):
    d = list(map(int, input().split()))
    data.append(d)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if data[i][j] == 1:



for i in range(4):
    XX = x+dx[i]
    YY = y+dy[i]
    if 테두리 안일때
        원하는 조건
