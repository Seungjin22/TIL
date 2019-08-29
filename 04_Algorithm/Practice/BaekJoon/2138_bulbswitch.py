import sys
sys.stdin = open('2138_input.txt')

T = 5
for tc in range(5):

    N = int(input())

    sample = list(map(int, input()))
    answer = list(map(int, input()))

    def switch():
        for i in range(N):
            sample[i] = not sample[i] or sample

