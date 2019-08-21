def bruteForce(p, t):
    M = len(p)
    N = len(t)
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return i - M    # 검색 성공
    else: return -1     # 검색 실패

def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt += 1
        if(cnt >= len(pattern)):
            return i
    return -1

text = "TTTTAACCA"
pattern = "TTA"
print("{}".format(bruteForce(pattern, text)))
print("{}".format(bruteForce2(text, pattern)))
print(text.find(pattern))