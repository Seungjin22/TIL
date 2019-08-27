import sys
sys.stdin = open('4874_input.txt')

def calc(formula):
    operator = '+-*/.'
    temp = []
    for f in formula:
        if f not in operator:
            temp.append(int(f))
        else:
            if f == '.' and len(temp) == 1:
                return temp.pop()
            elif len(temp) >= 2 and f != '.':
                b = temp.pop()
                a = temp.pop()
                if f == '+':
                    temp.append(a+b)
                elif f == '-':
                    temp.append(a-b)
                elif f == '*':
                    temp.append(a*b)
                elif f == '/':
                    temp.append(a//b)
            else:
                return 'error'

T = int(input())
for tc in range(1, T+1):
    formula = list(input().split())

    print('#{} {}'.format(tc, calc(formula)))