import sys
sys.stdin = open('5207_input.txt')


def BS(l, r, b, flag):
    global cnt
    m = (l+r) // 2
    if A[m] == b:
        cnt += 1
        return
    if l == r:
        return
    if A[m] < b:
        if flag == 1:
            return
        flag = 1
        BS(m + 1, r, b, flag)
    if A[m] > b:
        if flag == 2:
            return
        flag = 2
        BS(l, m - 1, b, flag)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split())) # A에 있는 수인지 확인
    cnt = 0
    for b in B:
        BS(0, len(A) - 1, b, 3)
    print('#{} {}'.format(tc, cnt))
