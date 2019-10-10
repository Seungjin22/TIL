import sys
sys.stdin = open('4873_input.txt')

def deleting(data):
    temp = []
    count = 0
    length = len(data)
    while True:
        if count >= length: return len(data)+len(temp)
        if data != []:
            a = data.pop()
        if temp != []:
            if a == temp[-1]:
                temp.pop()
            else:
                temp.append(a)
        else:
            temp.append(a)
        count += 1


T = int(input())
for tc in range(1, T+1):
    data = list(input())
    print('#{} {}'.format(tc, deleting(data)))