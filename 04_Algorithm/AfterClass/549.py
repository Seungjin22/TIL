n = int(input())
sum = 0
count = 0
for i in range(n):
    if i % 2:
        count += 1
        sum += i
        if sum >= n:
            break

print('{} {}'.format(count, sum))