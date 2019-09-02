import sys
sys.stdin = open('1227_input.txt')

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
            if a < 0 or a >= 100 or b < 0 or b >= 100: continue
            if maze[a][b] == 1: continue
            if visited[a][b] != 0: continue # continue를 사용해서 아닌 경우 다시 위로 올려버리기
            queue.append([a, b])
            visited[a][b] = 1
            if maze[a][b] == 3: return 1
    return 0

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    visited = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                si = i
                sj = j

    print('#{} {}'.format(tc, BFS(si, sj)))