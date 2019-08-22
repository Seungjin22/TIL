import sys
sys.stdin = open('midaverage_input.txt')

T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))
    num = sorted(num)

    avg = []
    for i in range(1, len(num)-1):
        avg.append(num[i])

    result = sum(avg) / len(avg)

    print('#{} {}'.format(tc, int(round(result, 0))))