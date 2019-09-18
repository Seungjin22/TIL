import sys
sys.stdin = open('5202_input.txt')


def dockdock(s, e):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    timetable = sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x: x[0])
    print(timetable)
    for i in range(len(timetable)):
        if timetable[i][0]