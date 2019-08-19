def itoa(x):
    str = list()
    i, y = 0, 0
    while True:
        y = x % 10
        str.append(chr(y + ord('0')))
        x //= 10
        if x == 0:
            break
        i += 1

    str.reverse()
    str = "".join(str)
    return str

x = 123
print(x, type(x))
str1 = itoa(x)
print(str1, type(str1))