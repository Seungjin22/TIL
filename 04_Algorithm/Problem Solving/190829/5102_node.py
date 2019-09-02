import sys
sys.stdin = open('5102_input.txt')

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while len(queue) != 0:
        v = queue.pop(0)
        for i in range(1, V+1): # 노드 시작점이 1이니까 V보다 하나 더 크게 잡기
            if data[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        data[i][j] = 1  # 방향성 없으니까 둘 다 잡아주기
        data[j][i] = 1

    S, G = map(int, input().split())
    BFS(S)
    if visited[G] == 0:
        result = 0
    else:
        result = visited[G] - 1
    print('#{} {}'.format(tc, result))

