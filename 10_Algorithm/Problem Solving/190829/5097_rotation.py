import sys
sys.stdin = open('5097_input.txt')

def rotation(M):
    for _ in range(M):
        num = data.pop(0)
        data.append(num)
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    rotation(M)

    print('#{} {}'.format(tc, data[0]))




# deque 사용해보기

# import collections
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     data = list(map(int, input().split()))
#     deq = collections.deque(data)   # 초기화 해주는 것
#
#     for i in range(M): # M번 뒤로 보내기
#         deq.append(deq.popleft())
#
#     print('#{} {}'.format(tc+1, deq.popleft()))