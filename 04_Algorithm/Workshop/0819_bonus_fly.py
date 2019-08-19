import sys
sys.stdin = open('0819_bonus_fly.txt')

T = int(input())

def fly_killer(datas, M):
    for i in range(len(datas)-M-1):
        total = 0
        max = 0
        for j in range(len(datas)-M-1):
            for z in range(M):
                total += datas[i][j+M]
                total += datas[i+M][j]
                total -= datas[0][0]
        if total > max:
            max = total
    return max



for tc in range(1, T+1):
    N, M = map(int, input().split())
    datas = []
    for i in range(N):
        data = list(map(int, input().split()))
        datas.append(data)

    result = fly_killer(datas, M)
    print(result)