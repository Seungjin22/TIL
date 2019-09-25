import time
from time import strftime

start_time = time.time()
import sys
sys.stdin = open('(5250)최소비용_input.txt', 'r')
T = int(input())

def solve(N):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    D[0][0] = 0
    q = []              # 소비량이 갱신된 지역의 인접 지역 저장용
    q.append((0, 0))
    while q:            # 더이상 갱신되는 경우가 없을 때까지 반복
        t = q.pop(0)
        for i in range(4):
            nx = t[0] + dx[i]  # 이동할 인접 칸 좌표
            ny = t[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:  # 유효한 범위면
                diff = 0
                if H[nx][ny] > H[t[0]][t[1]]:
                    diff = H[nx][ny] - H[t[0]][t[1]]  # 높이 차이 계산
                if D[nx][ny] > (D[t[0]][t[1]] + diff + 1):  # 기존 비용보다 이동 비용이 적으면
                    D[nx][ny] = D[t[0]][t[1]] + diff + 1  # 비용 갱신
                    q.append((nx, ny))  # 주변도 갱신될 수 있으므로 저장
    return D[N - 1][N - 1]

for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for i in range(N)]  # 각 지역의 높이 정보
    D = [[987654321] * N for i in range(N)]  # 각 칸 까지의 최소 연료 소비량

    print('#{} {}'.format(tc, solve(N)))
print(time.time() - start_time, 'seconds')