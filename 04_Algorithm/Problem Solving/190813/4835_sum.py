import sys
sys.stdin = open("4835_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    data = list(map(int, input().split()))

    max_total = sum(data[:N[-1]])
    min_total = sum(data[:N[-1]])

    for i in range(0, N[0]-N[-1]+1):
        total = sum(data[i:i+N[-1]])
        if total >= max_total:
            max_total = total
        elif total <= min_total:
            min_total = total

    result = max_total - min_total

    print("#{} {}".format(test_case, result))

