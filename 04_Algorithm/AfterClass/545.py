num = list(map(int, input().split()))

mul3 = 0
mul5 = 0
for i in num:
    if i % 3 == 0:
        mul3 += 1
    if i % 5 == 0:
        mul5 += 1

print('Multiples of 3 : {}\nMultiples of 5 : {}'.format(mul3, mul5))

