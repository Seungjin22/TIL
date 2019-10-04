import sys
sys.stdin = open('거스름돈_input.txt')


def dfs(money, cnt):
    global ans
    if ans < cnt or money < 0: return

    if money == 0:
        if ans > cnt: ans = cnt

    else:
        for i in range(n):
            dfs(money - coin[i], cnt + 1)

m = int(input())
n = int(input())
coin = list(map(int, input().split()))
ans = 987654321

dfs(m, 0)

print(ans)