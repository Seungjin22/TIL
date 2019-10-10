import sys
sys.stdin = open('5201_input.txt')

def loading(M):
    visited = [0] * len(T)
    for i in range(len(W)):
        for j in range(len(T)):
            if len(transport) == M:
                return
            if W[i] <= T[j] and visited[j] == 0:
                transport.append(W[i])
                visited[j] = 1
                break

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split())) # N개 화물의 무게
    T = list(map(int, input().split())) # M개 트럭의 적재용량
    transport = []
    W = sorted(W)
    T = sorted(T)
    W.reverse()
    T.reverse()
    loading(M)
    print('#{} '.format(tc), end="")
    if transport == []:
        print(0)
    else: print(sum(transport))
