import time
from time import strftime

start_time = time.time()
import sys
sys.stdin = open('(5250)최소비용_input.txt', 'r')
T = int(input())
def minDistacne():
    min = 987654321
    mx, my = -1, -1
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0 and D[i][j] < min:
                min = D[i][j]
                mx, my = i, j
    return mx, my

def check(x, y):
    if x < 0 or y < 0 or x > N-1 or y > N-1: return False
    if visit[x][y] : return False
    return True

def solve(N):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    D[0][0] = 0

    while True:
        x, y = minDistacne()
        visit[x][y] = 1
        if  x == N-1 and y == N-1 : return
        for i in range(4):
            nx = x + dx[i]  # 이동할 인접 칸 좌표
            ny = y + dy[i]
            if check(nx, ny):  # 유효한 범위면
                diff = 0
                if H[nx][ny] > H[x][y]:
                    diff = H[nx][ny] - H[x][y]  # 높이 차이 계산
                if D[nx][ny] > (D[x][y] + diff + 1):  # 기존 비용보다 이동 비용이 적으면
                    D[nx][ny] = D[x][y] + diff + 1  # 비용 갱신


for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for i in range(N)]  # 각 지역의 높이 정보
    D = [[987654321] * N for _ in range(N)]  # 각 칸 까지의 최소 연료 소비량
    visit = [[0]*N for _ in range(N)]
    solve(N)
    print('#{} {}'.format(tc,D[N-1][N-1] ))
print(time.time() - start_time, 'seconds')