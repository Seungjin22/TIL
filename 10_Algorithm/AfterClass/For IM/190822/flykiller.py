import sys
sys.stdin = open('flykiller_input.txt')

T = int(input())

def sumsquare(i, j, M):
    total = 0
    for y in range(M):
        for z in range(M):
            total += datas[i+y][j+z]
    return total

def fly_killer(N, M):
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = sumsquare(i, j, M)
            if total > max:
                max = total
    return max

for tc in range(1, T+1):
    N, M = map(int, input().split())
    datas = []
    for i in range(N):
        data = list(map(int, input().split()))
        datas.append(data)

    result = fly_killer(N, M)
    print('#{} {}'.format(tc, result))