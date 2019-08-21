arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(arr)):
    # for j in range(len(arr[i])):
    #     if i<j:
    for j in range(i+1, len(arr[i])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()