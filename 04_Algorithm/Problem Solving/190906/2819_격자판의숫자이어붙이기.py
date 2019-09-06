import sys
sys.stdin = open('2819_input.txt')
"""
재귀함수를 쓸 때 global 변수 지정 조심하기
if num not in result:
    result.append(num)
이 방법은 시간을 오래 걸리게 함
result안을 다 한 번씩 확인해줘야하니까
==> 무조건 다 append한 후에 set() 해주기!
"""
def counting(i, j, num):
    num += data[i][j]
    if len(num) == 7:
        result.append(num)
        return
    for idx in range(4):
        a = i + dx[idx]
        b = j + dy[idx]
        if a < 0 or a >= 4 or b < 0 or b >= 4: continue
        counting(a, b, num)

T = int(input())
for tc in range(1, T+1):
    data = [list(input().split()) for _ in range(4)]
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        for j in range(4):
            counting(i, j, '')
    print('#{} {}'.format(tc, len(set(result))))