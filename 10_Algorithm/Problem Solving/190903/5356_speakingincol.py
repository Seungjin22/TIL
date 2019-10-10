import sys
sys.stdin = open('5356_input.txt')

T = int(input())
for tc in range(1, T+1):
    words = []
    maxx = 0
    for _ in range(5):
        words.append(input())
        if len(words[-1]) > maxx:
            maxx = len(words[-1])
    print('#{}'.format(tc), end=" ")
    for i in range(maxx):
        for j in range(5):
            if len(words[j]) > i:
                print(words[j][i], end="")
    print()