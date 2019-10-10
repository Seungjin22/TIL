import sys
sys.stdin = open('0820_workshop.txt')

T = 10

def palindrome2(datas, n):
    for i in range(100):
        for j in range(100-(n-1)):
            flag = 1
            for z in range(n//2):
                if datas[i][j+z] != datas[i][j+n-1-z]:
                    flag = 0
                    break
            if flag:
                return n

    for i in range(100):
        for j in range(100-(n-1)):
            flag = 1
            for z in range(n//2):
                if datas[j+z][i] != datas[j+n-1-z][i]:
                    flag = 0
                    break
            if flag:
                return n

for tc in range(1, T+1):
    test_case = int(input())
    datas = []
    for i in range(100):
        data = list(input())
        datas.append(data)

    max = 0
    for n in range(100, 0, -1):
        result = palindrome2(datas, n)
        if result != None and result > max:
            max = result
    print('#{} {}'.format(tc, max))
