import sys
sys.stdin = open('0819_workshop.txt')

T = 10

def palindrome(datas, n):
    cnt = 0
    for i in range(8):
        for j in range(8-(n-1)):
            flag = 1
            for z in range(n//2):
                if datas[i][j+z] != datas[i][j+n-1-z]:
                    flag = 0
                    break
            if flag:
                cnt += 1

    for i in range(8):
        for j in range(8-(n-1)):
            flag = 1
            for z in range(n//2):
                if datas[j+z][i] != datas[j+n-1-z][i]:
                    flag = 0
                    break
            if flag:
                cnt += 1
    return cnt

for tc in range(1, T+1):
    N = int(input())
    datas = []
    for i in range(8):
        data = list(input())
        datas.append(data)

    result = palindrome(datas, N)

    print('#{} {}'.format(tc, result))