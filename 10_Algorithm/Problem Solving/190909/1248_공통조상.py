import sys
sys.stdin = open('1248_input.txt')

def finding_root(T, i):
    if T:
        roots[i].append(T)
    else: return
    finding_root(tree[T][2], i)

def matching():
    i = 0
    while True:
        if roots[0][i] != roots[1][i]:
            return roots[0][i-1]
        i += 1

def counting(R):
    ans = 1
    if tree[R][0] != 0:
        ans += counting(tree[R][0])
    if tree[R][1] != 0:
        ans += counting(tree[R][1])
    return ans

T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[0 for _ in range(3)] for _ in range(V+1)]
    roots = [[], []]
    result = []
    for i in range(0, len(data)-1, 2):
        if tree[data[i]][0] != 0:
            tree[data[i]][1] = data[i+1]
        else:
            tree[data[i]][0] = data[i+1]
        tree[data[i+1]][2] = data[i]

    finding_root(A, 0)
    finding_root(B, 1)
    roots[0].reverse()
    roots[1].reverse()
    root = matching()
    print('#{} {} {}'.format(tc, root, counting(root)))