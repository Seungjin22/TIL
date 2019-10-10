import sys
sys.stdin = open('1493_input.txt')

def fixing(p):
    a = 1
    for i in range(1, 10001):
        a += i
        if p < a:
            return i, p-(a-i)
T = int(input())
for tc in range(1, T+1):
    p, q = map(int, input().split())
    fixp, farp = fixing(p)
    fixq, farq = fixing(q)

    # p 좌표 : (1+farp, fixp-farp)
    # q 좌표 : (1+farq, fixq-farq)
    # 구하고자 하는 값의 좌표 : (2+farp+farq, fixp-farp+fixq-farq)
    # x = 2+farp+farq
    # y = fixp-farp+fixq-farq

    fara = farp+farq+1
    fixa = fixp+fixq+1

    b = 1
    for i in range(1, 100001):
        b += i
        if i == fixa:
            final = b-i
            break
    print('#{} {}'.format(tc, final+fara))