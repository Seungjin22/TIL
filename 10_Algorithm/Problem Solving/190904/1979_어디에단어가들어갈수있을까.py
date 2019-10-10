import sys
sys.stdin = open('1979_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # WP = Words Puzzle
    WP = [list(map(int, input().split())) for _ in range(N)]
    for wp in WP:
        wp.append(0)
    WP.append([0 for _ in range(N+1)])
    ans = 0
    for j in range(N):
        col = 0
        for i in range(N):
            if WP[i][j] == 1:
                col += 1
            if WP[i][j] == 0:
                col = 0
            if col == K and WP[i+1][j] != 1:
                ans += 1
    for i in range(N):
        row = 0
        for j in range(N):
            if WP[i][j] == 1:
                row += 1
            if WP[i][j] == 0:
                row = 0
            if row == K and WP[i][j+1] != 1:
                ans += 1
    print('#{} {}'.format(tc, ans))