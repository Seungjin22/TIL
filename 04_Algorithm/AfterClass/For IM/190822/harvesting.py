import sys
sys.stdin = open('harvesting_input.txt')

T = int(input())

def area(N):
    total = 0
    mid = N//2
    start = mid
    end = mid
    for j in range(N):
        if j >= mid:
            total += sum(farm[j][start:end+1])
            start += 1
            end -= 1
        else:
            total += sum(farm[j][start:end+1])
            start -= 1
            end += 1
    return total


for tc in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        f = list(map(int, input()))
        farm.append(f)

    total = area(N)
    print('#{} {}'.format(tc, total))