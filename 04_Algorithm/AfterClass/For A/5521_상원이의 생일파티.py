import sys
sys.stdin = open('5521_input.txt')
def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while queue:
        # print(queue)
        v = queue.pop(0)
        for i in range(1, N+1):
            if data[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        data[a][b] = 1
    # for _ in range(len(data)):
    #     print(_,data[_])
    BFS(1)
    cnt = 0
    for visit in visited:
        if visit == 2 or visit == 3:
            cnt += 1
    print('#{} {}'.format(tc, cnt))