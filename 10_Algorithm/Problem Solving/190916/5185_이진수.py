import sys
sys.stdin = open('5185_input.txt')

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

def change(x):
    global bn
    if x == 0:
        binary.append(reverse(bn))
        bn = ''
        return
    b = x % 2
    bn += str(b)
    change(x // 2)

T = int(input())
for tc in range(1, T+1):
    N, H = input().split()
    N = int(N)
    binary = []
    bn = ''
    for h in H:
        x = arr.index(h)
        change(x)
    for i in range(len(binary)):
        binary[i] = '0'*(4-len(binary[i])) + binary[i]
    binary_num = ''.join(binary)
    print('#{} {}'.format(tc, binary_num))