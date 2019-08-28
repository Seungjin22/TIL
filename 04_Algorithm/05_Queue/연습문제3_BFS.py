def BFS(v):
    queue = []
    queue.append(v)
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        v = queue.pop()
        for i in range(1, V+1):
            if G[v][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(i, end=" ")

import sys
sys.stdin = open('연습문제3_BFS.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
for i in range(V+1):
    print('{} {}'.format(i, G[i]))
BFS(1)

"""
1번 정점에서 가장 멀리 떨어져 있는 정점과 거리를 출력하시오.
답 : (6 3)

visited : [0, 1, 2, 2, 3, 3, 4, 3] 여기서 하나 빼야!
최댓값인 4 - 1 == 3
그 인덱스 6

visited[i] = visited[v] + 1
이렇게만 하면 구할 수 있음
"""