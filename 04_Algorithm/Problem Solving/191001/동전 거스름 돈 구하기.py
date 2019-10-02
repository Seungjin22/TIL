C = [[0 for _ in range(21)] for _ in range(5)]
D = [0, 1, 5, 10, 16]

for i in range(21):
    C[0][i] = 100

for i in range(1, 5):
    for j in range(1, 21):
        if j < D[i]:
            C[i][j] = C[i - 1][j]
        else:
            C[i][j] = min(C[i][j - D[i]] + 1, C[i - 1][j])

for i in range(1, 5):
    for j in range(1, 21):
        print('%2d ' % C[i][j], end="")
    print()

print('%d coins' % C[4][20])