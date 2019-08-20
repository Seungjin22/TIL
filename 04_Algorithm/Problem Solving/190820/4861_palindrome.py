import sys
sys.stdin = open('4861_input.txt')

T = int(input())

def palindrome(datas, N, M):
    result = ''
    for i in range(N):
        for j in range(N - (M - 1)):
            flag = 1
            for z in range(M // 2):
                if datas[i][j + z] != datas[i][j + M - 1 - z]:
                    flag = 0
                    break
            if flag:
                for z in range(M):
                    result += datas[i][j+z]


    for i in range(N):
        for j in range(N - (M - 1)):
            flag = 1
            for z in range(M // 2):
                if datas[j + z][i] != datas[j + M - 1 - z][i]:
                    flag = 0
                    break
            if flag:
                for z in range(M):
                    result += datas[j+z][i]

    return result

for tc in range(1, T+1):
    N, M = map(int, input().split())

    datas = []
    for i in range(N):
        data = list(input())
        datas.append(data)

    result = palindrome(datas, N, M)
    print('#{} {}'.format(tc, result))