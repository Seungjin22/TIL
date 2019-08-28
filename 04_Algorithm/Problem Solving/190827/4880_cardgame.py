import sys
sys.stdin = open('4880_input.txt')

def game(i, j):
    if i == j:
        return i
    else:
        a = game(i, (i+j)//2)
        b = game((i+j)//2+1, j)

        if cards[a] == cards[b]:
            return a
        else:
            if cards[a] == '1':
                if cards[b] == '2':
                    return b
                elif cards[b] == '3':
                    return a
            elif cards[a] == '2':
                if cards[b] == '3':
                    return b
                elif cards[b] == '1':
                    return a
            elif cards[a] == '3':
                if cards[b] == '1':
                    return b
                elif cards[b] == '2':
                    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = [0]+list(input().split())

    print('#{} {}'.format(tc, game(1, N)))