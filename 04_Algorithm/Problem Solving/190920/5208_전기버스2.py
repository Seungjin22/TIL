import sys
sys.stdin = open('5208_input.txt')


def Charging(i, cnt):
    global min
    if cnt > min: return
    if i >= N:
        if cnt < min:
            min = cnt
        return

    for x in range(M[i], 0, -1):
        Charging(i + x, cnt + 1)


for tc in range(1, int(input()) + 1):
    M = list(map(int, input().split()))
    N = M[0]
    min = 987654321
    Charging(1, 0)
    print('#{} {}'.format(tc, min - 1))