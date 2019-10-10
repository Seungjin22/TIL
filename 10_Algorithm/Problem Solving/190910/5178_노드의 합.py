import sys
sys.stdin = open('5178_input.txt')

def adding(T):
    if T > N: return
    adding(T * 2)
    adding(T * 2 + 1)
    if tree[T]:
        tree[T // 2] += tree[T]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        tree[x] = y
    adding(1)
    print('#{} {}'.format(tc, tree[L]))