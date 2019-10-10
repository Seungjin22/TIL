import sys
sys.stdin = open("4839_input.txt")

T = int(input())

def binarySearch(l, r, c):
    count = 0
    while l <= r:
        mid = (l + r)//2
        count += 1
        if mid == c:
            return count
        elif mid > c:
            r = mid
        else:
            l = mid

for test_case in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    countA = binarySearch(1, P, Pa)
    countB = binarySearch(1, P, Pb)
    if countA < countB:
        result = 'A'

    elif countA > countB:
        result = 'B'

    else:
        result = 0

    print('#{} {}'.format(test_case, result))