import sys
sys.stdin = open('5249_input.txt')


def MST_PRIM():
    total = 0
    u = 0   # 시작점
    D[u] = 0    # 가중치

    for i in range(V + 1):
        min = 987654321 # 무한대
        for v in range(V + 1):
            if visit[v] == 0 and min > D[v]:
                min = D[v]
                u = v

        visit[u] = 1    # 방문처리
        total += adj[PI[u]][u]

        for v in range(V + 1):  # 인접한 정점 업데이트
            if adj[u][v] != 0 and visit[v] == 0 and adj[u][v] < D[v]:
                D[v] = adj[u][v]
                PI[v] = u
    return total


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    adj = [[0] * (V+1) for _ in range(V+1)]
    D = [987654321] * (V+1)
    PI = list(range(V+1))
    visit = [0] * (V+1)
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    print('#{} {}'.format(tc, MST_PRIM()))