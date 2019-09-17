import sys
sys.stdin = open('연습문제2_input.txt')

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def change(x):
    global bn
    if x == 0:
        binary.append(bn)
        bn = ''
        return
    b = x % 2
    bn += str(b)
    change(x // 2)
digit = input()
binary = []
bn = ''
for d in digit:
    x = arr.index(d)
    change(x)
for i in range(len(binary)):
    binary[i] = '0'*(4-len(binary[i])) + binary[i]
print(binary)
binary_num = ''.join(binary)
print(binary_num)

num = ''
# for i in binary_num:
