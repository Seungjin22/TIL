arr = [1, 2, 3]
chk = [0] * 3


def OverPerm(d, rst):
    if len(rst) == 3:
        print(rst)
        return
    for i in range(len(arr)):
        OverPerm(d + 1, rst + [arr[i]])


def Perm(d, rst):
    if len(rst) == 3:
        print(rst)
        return
    for i in range(len(arr)):
        if not chk[i]:
            chk[i] = 1
            Perm(d + 1, rst + [arr[i]])
            chk[i] = 0


def Comb(d, rst):
    if len(rst) == 3:
        print(rst)
        return
    for i in range(d, len(arr)):
        Comb(i+1, rst + [arr[i]])


def OverComb(d, rst):
    if len(rst) == 3:
        print(rst)
        return
    for i in range(d, len(arr)):
        OverComb(i, rst + [arr[i]])


Perm(0, [])
print()
OverPerm(0, [])
print()
Comb(0, [])
print()
OverComb(0, [])