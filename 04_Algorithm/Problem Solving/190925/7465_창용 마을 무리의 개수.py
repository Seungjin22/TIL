import sys
sys.stdin = open('7465_input.txt')
"""
1 2 3 4 5 6
1 2 3 4 5 6 

1 2
2 5
5 1
3 4
4 6
찬환쓰가 메모장으로 알려준 방법
해당하는 인덱스의 값 중 더 작은 걸로 바꾸기
★ 주의할건 바뀐 후 그 숫자를 갖고 있는 다른 인덱스 확인해주기!!!
==> 예를 들어 1 1 3 3 1 3 에서 3 하나가 1로 바뀐다면 나머지 2개의 3도 1로 다 바꿔줘야 함
하나가 이어지면 그 그룹 다 이어지는거니까~
"""

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    town = list(range(N + 1))
    for _ in range(M):
        x, y = map(int, input().split())
        X = town[x]
        Y = town[y]
        if town[x] < town[y]:
            town[y] = X
            for i in range(N + 1):
                if town[i] == Y:
                    town[i] = X
        else:
            town[x] = Y
            for i in range(N + 1):
                if town[i] == X:
                    town[i] = Y
    town = set(town)
    print('#{} {}'.format(tc, len(town) - 1))
