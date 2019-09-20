def merge_sort(m):
    if len(m) == 1: return m

    left = []
    right = []
    middle = len(m) / 2
    for i in m:
        if m.index(i) < middle:
            left.append(i)
        else:
            right.append(i)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

m = [69, 10, 30, 2, 16, 8, 31, 22]

print(merge_sort(m))

