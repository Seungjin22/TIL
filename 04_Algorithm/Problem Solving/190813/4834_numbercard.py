import sys
from typing import List

sys.stdin = open("4834_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    data = str(input())

    card = [0] * 10

    for d in data:
        card[int(d)] += 1

    print(card)
    max_c = card[0]
    for idx, c in enumerate(card):
        if c >= max_c:
            max_c = c
            id = idx


    # result = []
    # if card.count(max_c) >= 1:
    #     for c in card:
    #         if c == max_c:
    #             result.append(card.index(c))



    print("#{} {} {}".format(test_case, id, max_c))