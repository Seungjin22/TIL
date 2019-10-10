import sys
sys.stdin = open('4871_input.txt')

def path(i, G):
    if result[0] == 1:
        return          # return한다고 끝나는게 X 한 칸 올라가는 것
    if i == G:
        result[0] = 1
    for j in range(len(data)):
        if data[i][j] == 1:
            path(j, G)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):
        i, j = map(int, input().split())
        data[i][j] = 1
    S, G = map(int, input().split())
    result = [0]
    path(S,G)
    print('#{} {}'.format(tc, result[0]))