import sys
sys.stdin = open('DFS_input.txt')

def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in range(V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

V, E = map(int, input().split()) # 정점(V), 간선(E)
temp = list(map(int, input().split()))

# 인접행렬(G)
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for i in range(V+1)]

# 입력
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1

# 입력 확인
for i in range(V+1):
    print('{} {}'.format(i, G[i]))

dfs(1)