import time
from time import strftime
start_time = time.time()

import sys
sys.stdin = open('1244_input.txt')
T = int(input())
MAXSIZE = 720
N = 10
def Swap(prize, i, j):
    #itoa
    numArr = [0] * numOfcard
    for k in range(numOfcard-1, -1, -1):
        numArr[k] = prize % 10
        prize //= 10
    numArr[i], numArr[j] = numArr[j], numArr[i]

    # atoi
    prize = 0
    for k in range(numOfcard):
        prize = prize * 10 + numArr[k]

    return prize


def findMax(prize, num, k):
    global ans
    for i in range(MAXSIZE):    # 가지치기. Memoization
        if memo[k][i] == 0:
            memo[k][i] = prize
            break
        elif memo[k][i] == prize:
            return

    if k == num:
        if prize > ans: ans = prize
    else:
        for i in range(numOfcard-1):
            for j in range(i+1, numOfcard):
                findMax(Swap(prize, i, j), num, k+1)


for tc in range(T):
    memo = [[0] * MAXSIZE for _ in range(N+1)]
    prize, num = map(int, input().split())      # 숫자판, 교환횟수
    numOfcard = 0                               # 숫자판의 숫자수
    ans = 0
    t = prize
    while(t):
        t //=10
        numOfcard += 1

    #### Greedy ####
    if num >= 6 :
        if num % 2 == 0 : num = 6
        else: num = 5

    findMax(prize, num, 0)

    print("#{} {}".format(tc+1, ans))

print(time.time() - start_time, 'seconds')


