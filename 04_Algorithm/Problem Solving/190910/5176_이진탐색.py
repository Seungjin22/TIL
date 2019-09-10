import sys
sys.stdin = open('5176_input.txt')

def saving(T):
    global cnt
    if T > N: return
    saving(T*2)
    tree[T] = cnt
    cnt+=1
    saving(T*2 + 1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    saving(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))