import sys
sys.stdin = open("0813_workshop.txt", "r")

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    def topbot(data):
        top = data[0]
        bot = data[0]
        bot_idx = 0
        top_idx = 0
        for idx, value in enumerate(data):
            if value > top:
                top = value
                top_idx = idx
            elif value < bot:
                bot = value
                bot_idx = idx
        return top, bot, top_idx, bot_idx

    for i in range(N):
        top, bot, top_idx, bot_idx = topbot(data)
        top -= 1
        data[top_idx] = top
        bot += 1
        data[bot_idx] = bot

    topbot(data)
    top, bot, top_idx, bot_idx = topbot(data)
    result = top - bot

    print(result)