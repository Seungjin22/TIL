import sys
sys.stdin = open("4831_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    oil = [0] * N

    while True:
        if