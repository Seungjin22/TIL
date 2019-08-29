import sys
sys.stdin = open('5097_input.txt')

def rotation(M):
    for _ in range(M):
        num = data.pop(0)
        data.append(num)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    rotation(M)

    print('#{} {}'.format(tc, data[0]))