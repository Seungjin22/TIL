import sys
sys.stdin = open('input.txt')

def coloring(x1, y1, x2, y2, color):
    global count
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            if paper[x][y] > color:
                return

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            paper[x][y] = color
    colors[color] = 0       # 인덴트 두 번 당김 확인하기

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    paper = [[0 for _ in range(M)] for _ in range(N)]

    colors = {0:0}
    for _ in range(K):
        count = 0
        x1, y1, x2, y2, color = map(int, input().split())
        coloring(x1, y1, x2, y2, color)

    for i in range(N):
        for j in range(M):
            if paper[i][j] in colors.keys():
                colors[paper[i][j]] += 1

    print('#{} {}'.format(tc, max(colors.values())))