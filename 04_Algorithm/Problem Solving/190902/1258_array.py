import sys
sys.stdin = open('1258_input.txt')

def squaring(i, j, n):
    for y in range(j, n):
        if array[i][y] == 0:
            width.append(y-j)
            break
    for x in range(i, n):
        if array[x][j] == 0:
            height.append(x-i)
            break
    for w in range(i, x):
        for z in range(j, y):
            visited[w][z] = 1

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    array = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    width = []
    height = []
    count = 0
    for i in range(n):
        for j in range(n):
            if array[i][j] != 0 and visited[i][j] == 0:
                count += 1
                squaring(i, j, n)

    sizes = []
    result = []
    for i in range(len(width)):
        size = width[i] * height[i]
        if size in sizes: continue
        sizes.append(size)
    sizes = sorted(sizes)
    for i in range(len(sizes)):
        for j in range(len(width)):
            if sizes[i] == width[j] * height[j]:
                result.append(height[j])
                result.append(width[j])

    area = 0
    for ans in range(0, len(result)-1, 2):
        if area == result[ans] * result[ans+1]:
            result[ans], result[ans-2] = result[ans-2], result[ans]
            result[ans+1], result[ans-1] = result[ans-1], result[ans+1]
        area = result[ans] * result[ans+1]

    print('#{} {}'.format(tc, count), end=" ")
    for ans in result:
        print('{}'.format(ans), end=" ")
    print()