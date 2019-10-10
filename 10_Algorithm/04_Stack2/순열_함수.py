import itertools
N = 3
for p in itertools.permutations(range(N)):
    for i in range(N):
        print(p[i], end=" ")
    print()

print()

N = 4
R = 3
for p in itertools.combinations(range(N), R):
    for i in range(R):
        print(p[i], end=" ")
    print()