import sys
sys.stdin = open('6109_input.txt')
def printArr(arr):
    for a in arr:
        print(a)
    print()

T = int(input())
for tc in range(1, T+1):
    N, S = input().split()
    N = int(N)
    TILE = [list(map(int, input().split())) for _ in range(N)]
    ANS = [[0 for _ in range(N)] for _ in range(N)]
    print('#{}'.format(tc))
    if S == 'up':
        final = []
        for j in range(N):
            Q = []
            for i in range(N):
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
            for _ in range(N-len(Q)):
                Q.append(0)
            final.append(Q)
        for j in range(N):
            for i in range(N):
                print(final[i][j], end=" ")
            print()

    elif S == 'down':
        final = []
        for j in range(N):
            Q = []
            for i in range(N - 1, -1, -1):
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
        for j in range(N - 1, -1, -1):
            for i in range(N):
                print(final[i][j], end=" ")
            print()

    elif S == 'right':
        final = []
        for i in range(N):
            Q = []
            for j in range(N - 1, -1, -1):
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
            for j in range(N-1, -1, -1):
                print(final[i][j], end=" ")
            print()

    elif S == 'left':
        final = []
        for i in range(N):
            Q = []
            for j in range(N):
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
            for j in range(N):
                print(final[i][j], end=" ")
            print()