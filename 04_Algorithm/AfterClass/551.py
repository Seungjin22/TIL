n = int(input())

for i in range(n):
    print('{}{}'.format(' '*i, '*'*(n-i)))