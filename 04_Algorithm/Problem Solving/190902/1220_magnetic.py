import sys
sys.stdin = open('1220_input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for j in range(100):
        queue = []
        for i in range(100):
            if table[i][j] == 0: continue
            if table[i][j] == 2 and len(queue) == 0:
                table[i][j] = 0
            if table[i][j] == 1:
                queue.append(table[i][j])
            if table[i][j] == 2 and queue[-1] == 1:
                queue.append(table[i][j])
                count += 1

    print('#{} {}'.format(tc, count))