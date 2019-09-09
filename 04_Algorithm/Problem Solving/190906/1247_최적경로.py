import sys
sys.stdin = open('1247_input.txt')
"""
일단 '순열'로 해야 함
ex) 회사 ==> {고객: 1, 2, 3} ==> 집
             고객 순서 순열로!
순열 함수가 제대로 작동하는지 확인하고 다음 코드 작성하기
"""

def perm(n, k):
    if k == n:
        calc()
    else:
        for i in range(k, n, 1):
            A[k], A[i] = A[i], A[k]

def calc():
    global ans
    dist = 0
    for i in range(N-1):


def delivery(key):
    Q = collections.deque()
    Q.append(key)
    visited[key] = customer[key]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    a = data[0::2]
    b = data[1::2]
    data = list(map(list, zip(a, b)))
    visited = [0 for _ in range(N)]
    cx, cy = data.pop(0)
    hx, hy = data.pop(0)
    customer = {}
    for i in range(N):
        customer[i+1] = data[i]
    print(customer)
