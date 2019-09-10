import sys
import collections
sys.stdin = open('1232_input.txt')

def post_order(T):
    if T:
        post_order(int(tree[T][2]))
        post_order(int(tree[T][3]))
        temp.append(tree[T][1])

for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3]
    for _ in range(N):
        t = input().split()
        tree.append(t)
    for tr in tree:
        if len(tr) < 4:
            for _ in range(4 - len(tr)):
                tr.append(0)
    temp = collections.deque()
    post_order(1)
    ans = []
    operators = ['+', '-', '*', '/']
    while len(temp) > 0:
        a = temp.popleft()
        if a in operators:
            y = ans.pop()
            x = ans.pop()
            if a == '-':
                ans.append(x - y)
            elif a == '+':
                ans.append(x + y)
            elif a == '*':
                ans.append(x * y)
            elif a == '/':
                ans.append(x // y)
        else:
            ans.append(int(a))

    print('#{} {}'.format(tc, ans[0]))

