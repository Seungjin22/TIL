def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent % 2 == 0:
        newbase = power(base, exponent/2)
        return newbase * newbase
    else:
        newbase = power(base, (exponent-1)/2)
        return (newbase * newbase) * base

print(power(2, 4))