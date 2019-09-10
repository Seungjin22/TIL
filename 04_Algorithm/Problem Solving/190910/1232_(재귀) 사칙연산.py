import sys
sys.stdin = open('1232_input.txt')

def inorder(x):
    if len(m[x]) == 1:
        return int(m[x][0])
    a = inorder(int(m[x][1]))
    b = inorder(int(m[x][2]))

    if m[x][0] == '+':
        return int(a) + int(b)
    elif m[x][0] == '-':
        return int(a) - int(b)
    elif m[x][0] == '*':
        return int(a) * int(b)
    elif m[x][0] == '/':
        return int(a) / int(b)

for testcase in range(1, 11):
    N = int(input())
    m = [[] for _ in range(N + 1)]
    for i in range(N):
        a = input().split()
        m[int(a[0])] = a[1:]
    print("#{} {}".format(testcase, int(inorder(1))))