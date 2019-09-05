import sys
sys.stdin = open('1974_input.txt')
def sudoku():
    for i in range(9):
        if sorted(SDK[i]) != nums:
            return 0
        temp = []
        for j in range(9):
            temp.append(SDK[j][i])
        if sorted(temp) != nums:
            return 0

    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            temp = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    temp.append(SDK[x][y])
            if sorted(temp) != nums:
                return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    SDK = [list(map(int, input().split())) for _ in range(9)]
    nums = list(range(1, 10, 1))
    print('#{} {}'.format(tc, sudoku()))