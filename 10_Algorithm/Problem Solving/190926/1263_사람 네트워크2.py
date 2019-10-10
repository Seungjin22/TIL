import sys
sys.stdin = open('1263_input.txt')


def AllPairsShortest(D):
    for k in range(N):
        for i in range(N):
            if i != k:
                for j in range(N):
                    if j != k and j != i:
                        D[i][j] = min(D[i][k] + D[k][j], D[i][j])

T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data.pop(0)
    dist = [[987654321] * N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            if data[idx]:
                dist[i][j] = data[idx]
            idx += 1

    AllPairsShortest(dist)

    mini = 987654321
    for i in range(N):
        if sum(dist[i]) < mini:
            mini = sum(dist[i])

    print('#{} {}'.format(tc, mini))
