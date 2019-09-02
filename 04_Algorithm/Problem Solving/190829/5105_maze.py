import sys
sys.stdin = open('5105_input.txt')

def BFS(si, sj):
    queue = []
    queue.append([si, sj])
    visited[si][sj] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while len(queue) != 0:
        i, j = queue.pop(0)
        for idx in range(4):
            a = i + dx[idx]
            b = j + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= N: continue
            if maze[a][b] == 1: continue
            if visited[a][b] != 0: continue # continue를 사용해서 아닌 경우 다시 위로 올려버리기
            queue.append([a, b])
            visited[a][b] = visited[i][j] + 1
            if maze[a][b] == 3: return visited[a][b]-2
    return 0    # 3 못만나거나 아닌 경우는 다 여기로 떨어져~

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # maze = []
    maze = [list(map(int, input())) for _ in range(N)] # 한 줄로 받아오기
    # for _ in range(N):
    #     m = list(map(int, input()))
    #     maze.append(m)
    visited = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

    print('#{} {}'.format(tc, BFS(si, sj)))
