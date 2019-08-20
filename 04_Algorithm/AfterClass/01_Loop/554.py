n = int(input())

alpha = ord('A')
num = 1
for i in range(n):
    for j in range(n-i, 0, -1 ):
        print('{}'.format(num), end=" ")
        num += 1
    count = 0
    for z in range(1, i+2):
        print('{}'.format(chr(alpha)), end=" ")
        alpha += 1
        count += 1
    print()