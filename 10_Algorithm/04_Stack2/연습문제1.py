"""
2+3*4/5
"""

formula = input()

nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = []

for f in formula:
    if f not in nums:
        operator.append(f)
    elif f in nums:
        print(f, end=" ")

for _ in range(len(operator)):
    print(operator.pop(), end=" ")

# while len(operator) != 0:
#     print(operator.pop(), end="")
