import sys
sys.stdin = open('5205_input.txt')

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)

def partition(A, l, r):
    p = A[l]
    i = l
    j = r
    while(i < j):
        while A[i] <= p and i < r:
            i += 1
        while A[j] >= p and j > l:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    quickSort(A, 0, len(A) - 1)
    print('#{} {}'.format(tc, A[N//2]))