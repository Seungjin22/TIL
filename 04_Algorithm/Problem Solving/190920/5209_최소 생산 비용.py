import sys
sys.stdin = open('5209_input.txt')


def Perm(d, rst, total):
    global mini
    if total > mini: return
    if len(rst) == N:
        if total < mini:
            mini = total
        return
    for i in range(len(arr)):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [arr[i]], total + V[d][i])
            chk[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    chk = [0] * N
    mini = 987654321
    Perm(0, [], 0)
    print('#{} {}'.format(tc, mini))