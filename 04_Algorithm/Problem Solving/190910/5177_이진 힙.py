import sys
sys.stdin = open('5177_input.txt')

def Heap(i):
    if i == 1:
        return
    if tree[(i) // 2] > tree[i]:
        tree[(i) // 2], tree[i] = tree[i], tree[(i) // 2]
        Heap((i) // 2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    tree = [0]*(N+1)
    for i in range(1, N+1):
        tree[i] = num[i-1]
        Heap(i)
    ans = 0
    while True:
        ans += tree[N//2]
        if (N//2) == 1: break
        N = N // 2
    print('#{} {}'.format(tc, ans))