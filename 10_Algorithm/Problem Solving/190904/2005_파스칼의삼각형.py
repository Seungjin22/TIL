import sys
sys.stdin = open('2005_input.txt')

def Pascal(N):
    for i in range(N):
        TRI[i][0] = 1
        if i >= 2:
            for j in range(1, N-1):
                TRI[i][j] = TRI[i-1][j-1] + TRI[i-1][j]
        for k in range(i+1):
            if TRI[i][k] == 0:
                TRI[i][k] = 1
                break
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    TRI = [[0 for _ in range(N)] for _ in range(N)]
    Pascal(N)
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if TRI[i][j] != 0:
                print(TRI[i][j], end=" ")
        print()