def check(data):
    right = ['0']
    left = []
    length = len(data)
    count = 0
    brackets = {']':'[', '}':'{', ')':'('}
    while True:
        if len(data) == 0 and len(right) == 1 and len(left) == 0: return 1
        if count >= length and len(right) != 1 or left != []: return 0
        if len(data) != 0:
            a = data.pop()
        if a in brackets.keys():
            right.append(a)
        elif a in brackets.values():
            if a == brackets.get(right[-1]):
                right.pop()
            else: left.append(a)
        count += 1


import sys
sys.stdin = open('4866_input.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input())

    print('#{} {}'.format(tc, check(data)))

