import sys
sys.stdin = open("4843_input.txt")

T = int(input())

def selectionSort(a):
    for i in range(0, len(a)-1):
        max = i
        min = i
        if i % 2:
            for j in range(i + 1, len(a)):
                if a[min] > a[j]:
                    min = j
            a[i], a[min] = a[min], a[i]

        else:
            for j in range(i+1, len(a)):
                if a[max] < a[j]:
                    max = j
            a[i], a[max] = a[max], a[i]

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    selectionSort(data)

    print('#{}'.format(test_case), end = " ")
    count = 0
    for i in data:
        count += 1
        print(i, end = " ")
        if count >= 10:
            break
    print()