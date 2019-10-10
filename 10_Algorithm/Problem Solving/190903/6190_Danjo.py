import sys
sys.stdin = open('6190_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    num = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            num.append(str(nums[i] * nums[j]))
    num = set(num)
    final = []
    flag = 0
    for i in num:
        flag = 1
        for j in range(len(i)-1):
            if i[j] > i[j+1]:
                flag = 0
                break
        if flag: final.append(int(i))
    if final:
        result = max(final)
    else:
        result = -1

    print('#{} {}'.format(tc, result))