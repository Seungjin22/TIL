import sys
sys.stdin = open('0826_workshop.txt')

operator = ['+', '-', '*', '/']

for tc in range(1, 11):
    oper = []
    mid = []
    result = []
    N = int(input())
    formula = input()

    for f in formula:
        if f == '(':
            oper.append(f)
        elif f == ')':
            while oper[-1] != '(':
               mid.append(oper.pop())
            oper.pop()
        elif f not in operator and f != ')' and f != '(':
            mid.append(f)
        elif f == '+' or f == '-':
            if oper[-1] == '(' or oper[-1] == '-' or oper[-1] == '+':
                oper.append(f)
            else:
                while oper[-1] != '(' or oper[-1] == '-' or oper[-1] == '+':
                    mid.append(oper.pop())
                oper.append(f)
        else:
            oper.append(f)

    for m in mid:
        if m not in operator:
            result.append(int(m))
        elif m in operator:
            b = result.pop()
            a = result.pop()
            if m == '+':
                result.append(a+b)
            elif m == '-':
                result.append(a-b)
            elif m == '*':
                result.append(a*b)
            elif m == '//':
                result.append(a/b)

    print('#{} {}'.format(tc, result.pop()))