import sys
sys.stdin = open('4869_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(N)] for _ in range(20)]
