import sys
sys.stdin = open('6109_input.txt')
def GameA(N, S):
    if S == 'up':
        M = range(N)
    elif S == 'down':
        M = range(N - 1, -1, -1)
    final = []
    for j in range(N):
        Q = []
        for i in M:
            if TILE[i][j] != 0 and Q == []:
                Q.append(TILE[i][j])
                flag = 0
            elif TILE[i][j] != 0 and Q != []:
                if Q[-1] == TILE[i][j]:
                    if flag == 0:
                        Q[-1] *= 2
                        flag = 1
                    elif flag == 1:
                        Q.append(TILE[i][j])
                        flag = 0
                else:
                    Q.append(TILE[i][j])
                    flag = 0
        for _ in range(N - len(Q)):
            Q.append(0)
        final.append(Q)
    for j in M:
        for i in range(N):
            print(final[i][j], end=" ")
        print()

def GameB(N, S):
    if S == 'right':
        M = range(N - 1, -1, -1)
    elif S == 'left':
        M = range(N)
    final = []
    for i in range(N):
        Q = []
        for j in M:
            if TILE[i][j] != 0 and Q == []:
                Q.append(TILE[i][j])
                flag = 0
            elif TILE[i][j] != 0 and Q != []:
                if Q[-1] == TILE[i][j]:
                    if flag == 0:
                        Q[-1] *= 2
                        flag = 1
                    elif flag == 1:
                        Q.append(TILE[i][j])
                        flag = 0
                else:
                    Q.append(TILE[i][j])
                    flag = 0
        for _ in range(N - len(Q)):
            Q.append(0)
        final.append(Q)
    for i in range(N):
        for j in M:
            print(final[i][j], end=" ")
        print()

T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    TILE = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(tc))

    if S == 'up' or S == 'down':
        GameA(N, S)
    elif S == 'right' or S == 'left':
        GameB(N, S)