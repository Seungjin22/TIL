import sys
sys.stdin = open("0814_workshop.txt", "r")


T = 10
for tc in range(T):
    test_case = int(input())
    col = 100
    row = 100
    # data = [[0 for _ in range(col)] for _ in range(row)]
    data = [list(map(int, input().split())) for _ in range(row)]

    max_sum = 0
    for i in range(100):
        sums=0
        for j in range(100):
            sums += data[i][j]
        if sums > max_sum:
            max_sum = sums

    for i in range(row):
        sums=0
        for j in range(col):
            sums += data[j][i]
        if sums > max_sum:
            max_sum = sums

    sums = 0
    for i in range(100):
        sums += data[i][i]
    if sums > max_sum:
        max_sum = sums

    sums = 0
    for i in range(100):
        sums += data[i][99-i]
    if sums > max_sum:
        max_sum = sums

    print("#{} {}".format(test_case, max_sum))