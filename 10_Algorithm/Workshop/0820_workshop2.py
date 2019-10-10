import sys
sys.stdin = open('0820_workshop2.txt')

T = int(input())

for _ in range(T):
    tc, N = input().split()
    N = int(N)
    data = list(input().split())

    num = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

    nums = []
    for i in data:
        for key in num.keys():
            if i == num.get(key):
                nums.append(key)

    nums = sorted(nums)

    print(tc)
    for i in nums:
        print(num[i], end = " ")
    print()