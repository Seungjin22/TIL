import sys
sys.stdin = open('1247_input.txt')

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
    f
