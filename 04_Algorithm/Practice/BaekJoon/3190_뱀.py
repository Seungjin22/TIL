import sys
sys.stdin = open('3190_input.txt')

def printArr(arr):
    for i in arr:
        print(i)
    print()

# def Dummy(X, C):
#     for _ in range(X):
#         i

# 보드의 크기: N, 사과의 개수: K
N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
# 사과의 위치
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 'a'

L = int(input())
dx = [-1, 1, 0, 0] # 상/하/좌/우
dy = [0, 0, -1, 1]
# C : L(왼쪽) / D(오른쪽)
for k in range(L):
    X, C = input().split()
    X = int(X)

    if k == 0:
        i = 0
        j = 0
        idx = 3
        for _ in range(X):
            i += dx[idx]
            j += dy[idx]

    if C ==
