import sys
sys.stdin = open("4837_input.txt")

T = int(input())

for test_case in range(1, T+1):
    A = list(range(1, 13))
    N, K = map(int, input().split())
    result = 0

    for i in range(1, 1 << len(A)):
        sum = 0
        count = 0
        for j in range(len(A)):
            if i & (1 << j):
                sum += A[j]
                count += 1

        if sum == K and count == N:
            result += 1

    print("#{} {}".format(test_case, result))


