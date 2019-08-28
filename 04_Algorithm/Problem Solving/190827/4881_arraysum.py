import sys
sys.stdin = open('4881_input.txt')

def perm(n, k, total):
    global mini
    if mini < total: return     # 가지치기!!!!!

    if k == n:
        if mini > total: mini = total
    else:
        for i in range(k, n):
            idx[k], idx[i] = idx[i], idx[k]
            perm(n, k+1, total + data[k][idx[k]])
            idx[k], idx[i] = idx[i], idx[k]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = []
    for _ in range(N):
        d = list(map(int, input().split()))
        data.append(d)
    mini = 987654321
    idx = list(range(N))

    perm(N, 0, 0)

    print('#{} {}'.format(tc, mini))