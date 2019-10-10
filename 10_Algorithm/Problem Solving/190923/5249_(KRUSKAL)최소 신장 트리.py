import sys
sys.stdin = open('5249_input.txt')
"""
Kruskal's Algorithm

모든 정점을 독립적인 집합으로 만든다.

모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.

두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다.

시간 복잡도는 O(ElogV)
"""

def Make_Set(x):
    parent[x] = x    # p[x] : 노드 x의 부모 저장
    rank[x] = 0 # rank[x] : 루트 노드가 x인 트리의 랭크 값 저장

def Find_Set(x):
    if x != parent[x]:   # x가 루트가 아닌 경우
        parent[x] = Find_Set(parent[x])
    return parent[x]

def Union(x, y):
    Link(Find_Set(x), Find_Set(y))

def Link(x, y):
    # 짧은 트리의 루트가 긴 트리의 루트를 가리키게 만드는 것이 좋음
    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def MST_KRUSKAL():
    for v in range(V + 1):
        Make_Set(v)

    mst = []
    data.sort()
    total = 0
    for d in data:
        w, v, u = d

        if Find_Set(v) != Find_Set(u):
            Union(v, u)
            mst.append(d)
            total += w
    return total


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    data = []
    parent = {}
    rank = {}
    for i in range(E):
        n1, n2, w = map(int, input().split())
        data.append([w, n1, n2])

    print('#{} {}'.format(tc, MST_KRUSKAL()))