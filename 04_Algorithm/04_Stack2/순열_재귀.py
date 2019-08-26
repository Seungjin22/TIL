def PrintArr(n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

def perm(n, k):
    if k == n:
        PrintArr(n)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

arr = [1, 2, 3]
perm(3, 0)