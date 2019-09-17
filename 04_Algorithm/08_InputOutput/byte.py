import sys
sys.stdin = open('byte_input.txt')

temp = input()
byte = ''


for i in range(len(temp)//7):
    print(int(temp[i*7:(i+1)*7], 2), end=",")


# for i in range(10):
#     n = 0
#     for j in range(i*7, i*7+7, 1):
#         n = n * 2 + arr[j]
#     print(n, end = " ")
# print()