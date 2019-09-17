import sys
sys.stdin = open('input.txt')

T = int(input())
N, M = map(int, input().split())
nana = []
for _ in range(N):
    n = input()
    nana.append(n)

print(T)
print('{} {}'.format(N, M))
for na in nana:
    print(na)