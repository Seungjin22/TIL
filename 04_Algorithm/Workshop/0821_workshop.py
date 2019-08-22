# Ladder
import sys
sys.stdin = open('0821_workshop.txt')

def ladder(datas, N):
   start = []
   for i in range(N):
       if datas[0][i] == 1:
           start.append(i)
   for xsis in range(len(start)):  #시작점 하나씩 출발하면서 비교, X좌표가 움직이기 때문에 바뀌지 않는 처음X위치 지정
       count = 1
       idx = xsis
       for j in range(count, N):
           if start[idx] != 99 and datas[j][start[idx]+1] == 1:
               idx += 1
           elif start[idx] != 0 and datas[j][start[idx]-1] == 1:
               idx -= 1
           if datas[j][start[idx]] == 2:
               return start[xsis]
T = 10
for _ in range(10):
   tc = int(input())
   datas = []
   for i in range(100):
       data = list(map(int, input().split()))
       datas.append(data)
   result = ladder(datas, 100)
   print('#{} {}'.format(tc, result))
# def ladder(datas, N):
#     start = []
#     for i in range(N):
#         if datas[0][i] == 1:
#             start.append(i)
#
#     idx = 0
#     while True:
#         count = 1
#         if start[idx] == 0:
#             for j in range(count, N):
#                 if datas[j][start[idx]+1] == 1:
#                     idx += 1
#                 elif start[idx] != 0 and datas[j][start[idx] - 1] == 1:
#                     idx -= 1
#                 if datas[j][start[idx]] == 2:
#                     return start[idx]
#                 count += 1
#         if start[idx] == 99:
#             start[idx] = start[idx]
#             for j in range(count, N):
#                 if start[idx] != 99 and datas[j][start[idx]+1] == 1:
#                     idx += 1
#                 elif datas[j][start[idx] - 1] == 1:
#                     idx -= 1
#                 if datas[j][start[idx]] == 2:
#                     return start[idx]
#                 count += 1
#         elif start[idx] != 0 and start[idx] != 99:
#             idx = 1
#             for j in range(count, N):
#                 if datas[j][start[idx]+1] == 1:
#                     idx += 1
#                 elif datas[j][start[idx]-1] == 1:
#                     idx -= 1
#                 if datas[j][start[idx]] == 2:
#                     return start[idx]
#                 count += 1


# def ladder(datas, N):
#     for i in range(N):
#         if datas[99][i] == 2:
#             start = i
#
#     count = N
#     for i in range(count, -1, -1):
#         count -= 1
#         datas[i][start]


# T = 10
# for _ in range(10):
#     tc = int(input())
#
#     datas = []
#     for i in range(100):
#         data = list(map(int, input().split()))
#         datas.append(data)
#
#     result = ladder(datas, 100)
#
#     print('#{} {}'.format(tc, result))

# def isWall(x, y):
#     if x < 0 or x >= 100: return True
#     if y < 0 or y >= 100: return True
#     if data[x][y] == 0: return True
#     if visited[x][y] == 1: return True
#     return False
#
#
# def haa(x, y):
#     visited[x][y] = 1
#     if data[x][y] == 2: return True
#     for z in range(3):
#         testX = x + dx[z]
#         testY = y + dy[z]
#         if isWall(testX, testY) == False:
#             return haa(testX, testY)


# for tc in range(10):
#     data = [[0 for _ in range(100)] for _ in range(100)]
#     visited = [[0 for _ in range(100)] for _ in range(100)]
#     T = input()
#     for i in range(100):
#         data[i] = list(map(int, input().split()))
#
#     dx = [0, 0, 1]
#     dy = [1, -1, 0]
#     x = 0
#     for y in range(100):
#         visited = [[0 for _ in range(100)] for _ in range(100)]
#         if data[x][y] == 1:
#             if haa(x, y):
#                 print('#{} {}'.format(T, y))



    # def check(data, x, y):
    #     if x < 0 or x >= SIZE: return False
    #     if y < 0 or y >= SIZE: return False
    #     if data[x][y] == 0: return False
    #     if data[x][y] == 9: return False # 방문표시
    #     return True
    #
    # def solve(data):
    #     x, y, newX, newY = 0, 0, 0, 0
    #     dx = [0, 0, -1] # 좌우를 먼저 해야 함
    #     dy = [-1, 1, 0]
    #
    #     for i in range(10): # 시작점 좌표 값 설정
    #         if data[SIZE-1][i] == 2:
    #             x = SIZE - 1
    #             y = i
    #             break
    #
    #     while True:
    #         if x == 0: return y
    #         for i in range(3):
    #             newX = x + dx[i]
    #             newY = y + dy[i]
    #             if check(data, newX, newY):
    #                 x = newX
    #                 y = newY
    #                 if data[x][y] == 9:
    #                     break
