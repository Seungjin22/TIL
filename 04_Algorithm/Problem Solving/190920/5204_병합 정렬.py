import sys
sys.stdin = open('5204_input.txt')

def merge_sort(m):
    if len(m) == 1: return m
    left = m[0:len(m)//2]
    right = m[len(m)//2:len(m)]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt
    result = []
    if left[-1] > right[-1]:
        cnt += 1
    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(left) > i:
            result.append(left[i])
            i += 1
        elif len(right) > j:
            result.append(right[j])
            j += 1
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = 0
    L = merge_sort(L)
    print('#{} {} {}'.format(tc, L[N//2], cnt))