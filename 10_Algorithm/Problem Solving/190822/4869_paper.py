import sys
sys.stdin = open('4869_input.txt')

def f(k):
    if k <=1 :
        return 1
    else:
        return f(k-1) + 2*f(k-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print("#{} {}".format(tc, f(N // 10)))