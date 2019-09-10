import sys
sys.stdin = open('5174_input.txt')

def counting(T):
    ans = 1
    if tree[T][0] != 0:
        ans += counting(tree[T][0])
    if tree[T][1] != 0:
        ans += counting(tree[T][1])
    return ans

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(E+2)]
    for i in range(0, len(node)-1, 2):
        if tree[node[i]][0] != 0:
            tree[node[i]][1] = node[i+1]
        else:
            tree[node[i]][0] = node[i+1]
        tree[node[i+1]][2] = node[i]

    print('#{} {}'.format(tc, counting(N)))