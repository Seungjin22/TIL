import sys
sys.stdin = open('1486_input.txt')

def calc(n, k, cursum):
    global ans
    if cursum >= B:
        if ans> cursum:
            ans = cursum
        return

def powerset(n, k, cursum):
    if ans < cursum: return

    if n == k:
        calc(n, k, cursum)
    else:
        A[k] = 1
        powerset(n, k + 1, cursum + h[k])
        A[k] = 0
        powerset(n, k + 1, cursum)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    A = [0] * N
    ans = 0xfffffff
    powerset(N, 0, 0)

    print("#%d %d" % (tc, ans - B))