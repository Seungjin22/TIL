import sys
sys.stdin = open('2138_input.txt')

T = 5
for tc in range(5):

    N = int(input())

    sample = list(map(int, input()))
    answer = list(map(int, input()))

    def switchOnOff(sample, i):
        if i == 0:
            sample[i] = not sample[i]
            sample[i+1] = not sample[i+1]
        elif i == N-1:
            sample[i-1] = not sample[i-1]
            sample[i] = not sample[i]
        elif i != 0 and i != N-1:
            sample[i - 1] = not sample[i - 1]
            sample[i] = not sample[i]
            sample[i + 1] = not sample[i + 1]

        return sample

    count = 0
    while sample != answer:
        for i in range(1, N-1):
            if sample[i-1]^answer[i-1] == 1:
                count += 1
                sample = switchOnOff(sample, i-1)
            else:
                continue
            if sample[i-1] == sample[i] == sample[i+1] and answer[i-1] == answer[i] == answer[i+1] and \
                    sample[i] ^ answer[i] == 1:
                sample = switchOnOff(sample, i)
                if sample == answer:
                    break

    print(count)