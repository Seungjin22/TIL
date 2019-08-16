#1. 
'''
n개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 값이 몇 번째 수인지 구하세요.

예를 들어, 서로 다른 n개의 자연수가 [3, 29, 38, 12, 57, 74, 40, 85, 61] 이라면
최댓값은 85, 7번째 수

answer = [85, 7]
'''



# def my_max(lists):
#     number = []
#     for i in lists:
#         number.append(i)
#     return max(number)


answer = []

def my_max2(lists):
    max_num = lists[0]
    for i in lists:
        if max_num < i:
            max_num = i
    return max_num

nums = [3, 29, 38, 12, 57, 74, 40, 85, 61]

for idx, value in enumerate(nums):
    if value == my_max2(nums):
        answer.append(value)
        answer.append(idx)
        break

print(f'answer = {answer}')

