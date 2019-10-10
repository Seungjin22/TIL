#10개의 정수 입력받아 부분집합의 합이 10이 되는 것이 존재하는지를 계산하는 함수 작성
sum = 0
arr = list(map(int, input().split()))
for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
           sum += arr[j]

    if sum == 10:
        for j in range(len(arr)):
            if i & (1 << j):
                print(arr[j], end=" ")
        print()