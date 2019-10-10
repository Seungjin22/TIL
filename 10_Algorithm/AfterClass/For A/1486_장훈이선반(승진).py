import sys
sys.stdin = open('1486_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
