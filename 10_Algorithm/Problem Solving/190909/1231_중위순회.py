import sys
sys.stdin = open('1231_input.txt')

def in_order(T):
    if T:
        in_order(int(tree[T][2]))
        print(tree[T][1], end="")
        in_order(int(tree[T][3]))

for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0, 0]]
    for _ in range(N):
        d = list(input().split())
        tree.append(d)
    for t in tree:
        if len(t) < 4:
            for _ in range(4-len(t)):
                t.append(0)
    print('#{}'.format(tc), end=" ")
    in_order(1)
    print()