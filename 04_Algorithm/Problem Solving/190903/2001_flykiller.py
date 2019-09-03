import sys
sys.stdin = open('2001_input.txt')

def fkiller(i, j, M):
    total = 0
    for x in range(i, i+M):
        for y in range(j, j+M):
            total += fly[x][y]
    return total


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = fkiller(i, j, M)
            if total > max:
                max = total

    print('#{} {}'.format(tc, max))