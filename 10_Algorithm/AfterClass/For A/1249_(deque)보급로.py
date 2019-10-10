import sys
import collections
sys.stdin = open('1249_input.txt')
def path(N, i, j):
    Q = collections.deque()
    Q.append((i, j))
    visited[i][j] = MAP[i][j]
    if i == N-1 and j == N-1: return
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while Q:
        i, j = Q.popleft()
        for idx in range(4):
            a = i + dx[idx]
            b = j + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= N: continue
            if MAP[a][b] + visited[i][j] < visited[a][b]:
                visited[a][b] = MAP[a][b] + visited[i][j]
                Q.append((a, b))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    visited = [[987654321 for _ in range(N)] for _ in range(N)]
    path(N, 0, 0)
    print('#{} {}'.format(tc, visited[-1][-1]))