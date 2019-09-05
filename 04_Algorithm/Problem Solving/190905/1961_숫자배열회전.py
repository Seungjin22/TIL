import sys
sys.stdin = open('1961_input.txt')
def printArr(data):
    for k in range(4):
        for i in range(N):
            for j in range(N):
                print(data[k][i][j], end='')
            print()
        print()
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(4)]
    for i in range(N):
        data[0][i] = list(input().split())

    for k in range(3):
        for i in range(N):
            for j in range(N):
                data[k+1][j][i] = data[k][N-1-i][j]

    print('#{}'.format(tc))
    for i in range(N):
        for k in range(1, 4):
            print('{}'.format(''.join(data[k][i])), end=" ")
        print()