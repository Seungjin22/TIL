import sys
sys.stdin = open('2805_input.txt')
def harvest(N):
    total = 0
    mid = N // 2
    start = mid
    end = mid
    for i in range(N):
        if i >= mid:
            total += sum(farm[i][start:end+1])
            start += 1
            end -= 1
        else:
            total += sum(farm[i][start:end+1])
            start -= 1
            end +=1
    return total

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    print('#{} {}'.format(tc, harvest(N)))
