import sys
sys.stdin = open('1219_input.txt')

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while len(queue) != 0:
        v = queue.pop(0)
        for i in range(0, 100):
            if path[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1

for _ in range(10):
    tc, N = map(int, input().split())
    temp = list(map(int, input().split()))
    data = []
    for i in range(0, 2*N-1, 2):
        data.append([temp[i], temp[i+1]])
    path = [[0 for _ in range(100)] for _ in range(100)]
    visited = [0 for _ in range(100)]
    for i in data:
        x, y = i[0], i[-1]
        path[x][y] = 1

    BFS(0)
    if visited[99] == 0:
        result = 0
    else:
        result = 1
    print('#{} {}'.format(tc, result))


    # DFS로도 풀어보기