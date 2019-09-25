import sys
from collections import deque
sys.stdin = open('1861_input.txt')


def Move(i, j):
    global cnt
    stk = deque()
    stk.append([i, j])
    while(stk):
        i, j = stk.pop()
        for idx in range(4):
            a = i + dx[idx]
            b = j + dy[idx]
            if a < 0 or a >= N or b < 0 or b >= N: continue
            if A[i][j] + 1 != A[a][b]: continue
            cnt += 1
            stk.append([a, b])


for tc in range(1, int(input()) + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0
    max = 0
    s = []
    for i in range(N):
        for j in range(N):
            Move(i, j)
            if cnt >= max and cnt != 0:
                if cnt == max:
                    s.append(A[i][j])
                elif cnt > max:
                    s = []
                    s.append(A[i][j])
                max = cnt
            cnt = 0
    print('#{} {} {}'.format(tc, min(s), max + 1))