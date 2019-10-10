import sys
sys.stdin = open('4865_input.txt')

T = int(input())

def counting(str1, str2):
    data = {}
    for i in str2:
        if i not in data.keys():
            data[i] = 1
        else:
            data[i] += 1

    max = 0
    for key in data.keys():
        if key in str1 and data[key] > max:
            max = data[key]
    return max


for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = counting(str1, str2)

    print('#{} {}'.format(tc, result))
