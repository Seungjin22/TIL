def check_matching(data):
    stk = []
    for i in data:
        if i == '(':
            stk.append(i)
        elif i == ')':
            j = stk.pop()
            if j != '(':
                stk.append(j)

    if stk != []:
        return False

    else:
        return True


data = input()
print(check_matching(data))