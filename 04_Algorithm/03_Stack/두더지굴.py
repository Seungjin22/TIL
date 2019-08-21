import sys
sys.stdin = open('두더지.txt')

N = int(input())

datas = []
for i in range(N):
    data = list(map(int, input().split()))
    datas.append(data)

