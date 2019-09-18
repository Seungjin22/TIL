import sys
sys.stdin = open('5189_input.txt')

def Perm(d, rst):
    if len(rst) == N:
        rst += [1]
        paths.append(rst)
        return
    for i in range(N-1):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [temp[i]])
            chk[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    temp = list(range(2, N + 1))
    chk = [0] * (N-1)
    paths = []
    Perm(0, [1])
    min = 987654321
    for i in paths:
        ans = 0         # ans 초기화 시켜주기 ★
        for j in range(len(i) - 1):
            ans += area[i[j]-1][i[j+1]-1]   # 문제에서 주어진 1부터는 사실상 data에서 0부터!!!
        if ans < min:
            min = ans
    print('#{} {}'.format(tc, min))
