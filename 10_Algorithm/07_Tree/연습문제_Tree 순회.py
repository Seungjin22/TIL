import sys
sys.stdin = open('연습문제_input.txt')

def pre_order(T):
    if T:
        print(T, end=" ")
        pre_order(tree[T][0])
        pre_order(tree[T][1])

def in_order(T):
    if T:
        in_order(tree[T][0])
        print(T, end=" ")
        in_order(tree[T][1])

def post_order(T):
    if T:
        post_order(tree[T][0])
        post_order(tree[T][1])
        print(T, end=" ")

N = int(input())
node = list(map(int, input().split()))
tree = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(0, len(node) - 1, 2):
    if tree[node[i]][0] != 0:
        tree[node[i]][1] = node[i+1]
    else:
        tree[node[i]][0] = node[i+1]
    tree[node[i + 1]][2] = node[i]

print('전위')
pre_order(1)
print()

print('중위')
in_order(1)
print()

print('후위')
post_order(1)
print()
