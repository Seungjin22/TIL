import sys
sys.stdin = open('5099_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    cooked = [0 for _ in range(M)]
    Cii = []
    for i in Ci:
        Cii.append(i)

    stove = []
    name = []

    for _ in range(N):
        pizza = Ci.pop(0)
        stove.append(pizza)
        name.append(pizza)

    while (len(stove) != 1):
        C = stove.pop(0)
        P = name.pop(0)
        if C//2 == 0:
            if len(Ci) == 0: continue
            pizza = Ci.pop(0)
            stove.append(pizza)
            name.append(pizza)
        else:
            stove.append(C//2)
            name.append(P)


    ans = []
    for id, i in enumerate(Cii):
        if i == name[0]:
            ans.append(id)

    print('#{} {}'.format(tc, ans[-1]+1))