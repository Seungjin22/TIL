import sys
sys.stdin = open('4864_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    result = 0
    for i in range(M-(N-1)):
        sample = ''
        for j in range(N):
            sample += str2[i+j]
        if sample == str1:
            result = 1
            break

    print('#{} {}'.format(tc, result))