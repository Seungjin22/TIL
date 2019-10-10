import sys
sys.stdin = open('5202_input.txt')
"""
종료 시간 순으로 정렬
cnt : 작업수
end : 앞 작업의 종료 시간
모든 작업에 대해 앞 작업 이후에 시작하면 작업을 추가하고 종료 시간을 새 작업으로 수정
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    timetable = sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x: x[1])
    cnt = 0
    end = 0
    for i in range(N):
        if end <= timetable[i][0]:
            cnt += 1
            end = timetable[i][1]
    print('#{} {}'.format(tc, cnt))