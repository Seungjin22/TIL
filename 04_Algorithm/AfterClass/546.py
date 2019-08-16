num = int(input())
scores = list(map(int, input().split()))

avg = sum(scores) / num
print('avg : {}'.format(round(avg, 1)))
if avg >= 80:
    print('pass')
else:
    print('fail')