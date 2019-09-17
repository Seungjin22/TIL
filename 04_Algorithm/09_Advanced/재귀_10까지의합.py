def SUM(n):

    if n == 1:
        return 1
    return n + SUM(n-1)

# def SSUM(n):
#     if n > 10:
#         return


print(SUM(10))