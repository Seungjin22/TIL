n = int(input())

alpha = ord('A')
for i in range(n):
    for j in range(n-i, 0, -1):
        print('{}'.format(chr(alpha)), end="")
        alpha += 1
    print()
