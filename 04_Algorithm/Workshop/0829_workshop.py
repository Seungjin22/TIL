import sys
sys.stdin = open('0829_workshop.txt')

def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    while len(queue) != 0:
        v = queue.pop(0)
        for i in range(1, 101):
            if contact[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[v] + 1

for tc in range(1, 11):
    N, S = map(int, input().split())
    d = list(map(int, input().split()))
    a = d[0::2]
    b = d[1::2]
    data = list(map(list, zip(a, b)))
    visited = [0 for _ in range(101)]
    contact = [[0 for _ in range(101)] for _ in range(101)]

    for i in data:
        x = i[0]
        y = i[1]
        contact[x][y] = 1

    BFS(S)
    result = []
    for i in visited:
        if i != 0:
            result.append(i)

    final = []
    for i in range(101):
        if visited[i] == max(result):
            final.append(i)

    print('#{} {}'.format(tc, max(final)))