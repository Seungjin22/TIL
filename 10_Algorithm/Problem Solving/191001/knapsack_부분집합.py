def powerset(n, k, curWeight, curValue):
    global ans
    if curWeight > W: return    # 현재 무게가 배낭 무게보다 크면

    if n == k:
        if ans < curValue: ans = curValue
    else:
        A[k] = 1
        powerset(n, k + 1, curWeight + weight[k], curValue + value[k])
        A[k] = 0
        powerset(n, k + 1, curWeight, curValue)


W = 10  # 배낭의 무게
n = 4   # 물건의 개수
weight = [5, 4, 6, 3]    # 물건들의 무게
value = [10, 40, 30, 50] # 물건들의 가치
A = [0] * n
ans = 0

powerset(n, 0, 0, 0)
print('%d' % (ans))