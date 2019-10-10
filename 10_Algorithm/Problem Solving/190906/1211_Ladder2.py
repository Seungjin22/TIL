import sys
sys.stdin = open('1211_input.txt')

def ladder(data, N):
    start = []
    for i in range(N):
        if data[0][i] == 1:
            start.append(i)
    mini = 987654321
    for xsis in range(len(start)):  #시작점 하나씩 출발하면서 비교, X좌표가 움직이기 때문에 바뀌지 않는 처음X위치 지정
        count = 0
        jj = 1
        idx = xsis
        for j in range(jj, N):
            count += 1
            if start[idx] != 99 and data[j][start[idx]+1] == 1:
                idx += 1
                count += (abs(start[idx] - start[idx-1]))
            elif start[idx] != 0 and data[j][start[idx]-1] == 1:
                idx -= 1
                count += (abs(start[idx] - start[idx+1]))

        if count < mini:
            mini = count
            result = start[xsis]
    return result

T = 10
for _ in range(10):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    result = ladder(data, 100)
    print('#{} {}'.format(tc, result))