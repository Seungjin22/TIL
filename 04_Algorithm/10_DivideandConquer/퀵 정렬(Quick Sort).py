def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)

def partition(A, l, r):
    p = A[l]
    i = l
    j = r
    while(i <= j):
        while A[i] <= p and i <= j:
            i += 1
        while A[j] >= p and j >= i:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

A = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quickSort(A, 0, len(A) - 1)
print(A)