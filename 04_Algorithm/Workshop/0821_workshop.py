# Ladder
import sys
sys.stdin = open('0821_workshop.txt')

# def ladder(datas, N):
#     start = []
#     for i in range(N):
#         if datas[0][i] == 1:
#             start.append(i)
#
#     count = 1
#     idx = 0
#     i = start[idx]
#
#     for j in range(count, N):
#         count += 1
#         if datas[j][i+1] == 1:
#             idx += 1
#         elif datas[j][i-1] == 1:
#             idx -= 1
#         if datas[j][i] == 2:
#             return i


def ladder(datas, N):
    for i in range(N):
        if datas[99][i] == 2:
            start = i

    count = N
    for i in range(count, -1, -1):
        count -= 1
        datas[i][start]


T = 10
for _ in range(10):
    tc = int(input())

    datas = []
    for i in range(100):
        data = list(map(int, input().split()))
        datas.append(data)

    result = ladder(datas, 100)

    print('#{} {}'.format(tc, result))

