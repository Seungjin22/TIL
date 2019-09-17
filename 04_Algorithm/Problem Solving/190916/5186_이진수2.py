import sys
sys.stdin = open('5186_input.txt')

def dectobin(n):
    cnt = 0
    ret = ''
    while cnt < 13:
        n *= 2
        if n == 1:
            ret += '1'
            break
        elif n > 1:
            ret += '1'
            n -= 1
        else:
            ret += '0'
        cnt += 1
    if len(ret) == 13:
        return 'overflow'
    else:
        return ret


T = int(input())
for testcase in range(1, T + 1):
    N = float(input())
    print("#{} {}".format(testcase, dectobin(N)))