import sys
sys.stdin = open("0816_workshop.txt")

# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     data = list(map(int, input().split()))

    # result = [[0 for _ in range(2)] for _ in range(n)]
    # print(result)
    #
    # x = 0
    # y = 0
    # for i in range(len(data)):
    #     if i % 2 == 0:
    #         result[x][0] = i
    #         x += 1
    #     else:
    #         result[0][y] = i
    #         y += 1
    #
    #
    #
    # print(result)


    # mom = []
    # i = 0
    # for _ in range(n):
    #     baby = []
    #     baby.append(data[i])
    #     baby.append(data[i+1])
    #     i += 2
    #     mom.append(baby)
    #
    # result = []
    # for i in range(n):
    #     for j in range(n):
    #         if mom[i][0] == mom[j][1]:
    #             result.append(mom[j][0])
    #             result.append(mom[j][1])
    #             result.append(mom[i][0])
    #             result.append(mom[i][1])
    # print(result)
    # mom = []
    # for i in data:
    #     baby = []
    #     for _ in range(2):
    #         baby.append(i)
    #     mom.append(baby)
    # print(mom)

T = int(input())
for tc in range(T):
    c = int(input())
    a = list(map(int, input().split()))
    b = {}
    c = []
    for k in range(0, len(a) - 1, 2):
        b[a[k]] = a[k + 1]

    for j in range(len(b)):
        for key, value in b.items():
            if not key in b.values():
                c.append(key)
                c.append(value)
        del (b[c[-2]])

    print('#{}'.format(tc + 1), end=' ')
    for i in range(len(c)):
        print(c[i], end=" ")
    print()