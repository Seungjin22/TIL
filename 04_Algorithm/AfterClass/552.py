n = int(input())

for i in range(n):
    print('{}{}{}'.format(' '*i, '*'*(n+2-(2*i)), ' '*i))